const formatPrice = (n) => n.toLocaleString('ru-RU') + ' ₽';

// Шапка при скролле
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 50);
});

// Бургер-меню
const burger = document.getElementById('burger');
const nav = document.getElementById('nav');
burger.addEventListener('click', () => {
  burger.classList.toggle('active');
  nav.classList.toggle('open');
});
nav.querySelectorAll('a').forEach((link) =>
  link.addEventListener('click', () => {
    burger.classList.remove('active');
    nav.classList.remove('open');
  })
);

// Каталог
const cardsEl = document.getElementById('cards');
const cards = [...cardsEl.querySelectorAll('.card')];

cards.forEach((card) => {
  const price = card.querySelector('.card__price');
  price.textContent = formatPrice(Number(card.dataset.price));
});

document.querySelectorAll('.filters__btn').forEach((btn) => {
  btn.addEventListener('click', () => {
    document.querySelector('.filters__btn.active').classList.remove('active');
    btn.classList.add('active');
    cards.forEach((card) => {
      card.hidden = btn.dataset.filter !== 'all' && card.dataset.category !== btn.dataset.filter;
    });
  });
});

// Модальное окно
const modal = document.getElementById('modal');
const carSelect = document.getElementById('carSelect');
let currentCar = null;

cardsEl.addEventListener('click', (e) => {
  const btn = e.target.closest('[data-car-details]');
  if (!btn) return;
  currentCar = btn.closest('.card');
  const image = document.getElementById('modalImg');
  image.src = currentCar.dataset.image;
  image.alt = currentCar.dataset.name;
  image.hidden = !currentCar.dataset.image;
  document.getElementById('modalTitle').textContent = currentCar.dataset.name;
  document.getElementById('modalPrice').textContent = formatPrice(Number(currentCar.dataset.price));

  const specs = document.getElementById('modalSpecs');
  specs.replaceChildren();
  [
    ['Год выпуска', currentCar.dataset.year],
    ['Двигатель', currentCar.dataset.engine],
    ['Коробка', currentCar.dataset.gearbox],
  ].forEach(([label, value]) => {
    const item = document.createElement('li');
    const detail = document.createElement('b');
    item.append(document.createTextNode(label), detail);
    detail.textContent = value;
    specs.append(item);
  });
  modal.classList.add('open');
});

const closeModal = () => modal.classList.remove('open');
document.getElementById('modalClose').addEventListener('click', closeModal);
modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

document.getElementById('modalBtn').addEventListener('click', () => {
  if (currentCar) carSelect.value = currentCar.name;
  closeModal();
});

// Кредитный калькулятор
const price = document.getElementById('price');
const down = document.getElementById('down');
const term = document.getElementById('term');
const RATE = 4.9;

function calcCredit() {
  const p = Number(price.value);
  const d = Number(down.value);
  const t = Number(term.value);
  const loan = p * (1 - d / 100);
  const r = RATE / 100 / 12;
  const monthly = loan * (r * Math.pow(1 + r, t)) / (Math.pow(1 + r, t) - 1);

  document.getElementById('priceOut').textContent = formatPrice(p);
  document.getElementById('downOut').textContent = `${d}% (${formatPrice(p * d / 100)})`;
  document.getElementById('termOut').textContent = `${t / 12} ${t === 12 ? 'год' : t < 60 ? 'года' : 'лет'}`;
  document.getElementById('monthly').textContent = formatPrice(Math.round(monthly));
}

[price, down, term].forEach((input) => input.addEventListener('input', calcCredit));

// Форма заявки
const form = document.getElementById('form');
const formMessage = document.getElementById('formMessage');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const { name, phone } = form.elements;
  const phoneValid = phone.value.replace(/\D/g, '').length >= 10;

  name.classList.toggle('error', !name.value.trim());
  phone.classList.toggle('error', !phoneValid);

  if (!name.value.trim() || !phoneValid) {
    formMessage.className = 'form__message error';
    formMessage.textContent = 'Пожалуйста, укажите имя и корректный телефон';
    return;
  }

  formMessage.className = 'form__message success';
  formMessage.textContent = `Спасибо, ${name.value.trim()}! Мы перезвоним вам в ближайшее время.`;
  form.reset();
});

// Анимация счётчиков
function animateCounters() {
  document.querySelectorAll('[data-count]').forEach((el) => {
    const target = Number(el.dataset.count);
    const duration = 1500;
    const start = performance.now();
    const step = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      el.textContent = Math.floor(progress * target).toLocaleString('ru-RU');
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  });
}

// Старт
document.getElementById('year').textContent = new Date().getFullYear();
calcCredit();
animateCounters();
