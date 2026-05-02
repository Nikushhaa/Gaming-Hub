// ================================================
//  GAMING HUB — script.js
//  Features:
//    1. Mobile menu toggle
//    2. Header scroll effect
//    3. Smooth scroll for nav links
//    4. Game search + category filter
//    5. Contact form validation
//    6. Back-to-top button
// ================================================


// ---- 1. GRAB ELEMENTS WE NEED ----

// Header and mobile menu
const header     = document.getElementById('header');
const menuBtn    = document.getElementById('menuBtn');
const mobileNav  = document.getElementById('mobileNav');

// Search and filter
const searchInput  = document.getElementById('searchInput');
const filterBtns   = document.querySelectorAll('.filterBtn');
const gameCards    = document.querySelectorAll('.gameCard');
const noResults    = document.getElementById('noResults');

// Contact form
const form1        = document.getElementById('form1');
const inputName    = document.getElementById('inputName');
const inputEmail   = document.getElementById('inputEmail');
const inputSubject = document.getElementById('inputSubject');
const inputMessage = document.getElementById('inputMessage');
const formSuccess  = document.getElementById('formSuccess');

// Back to top button
const backToTop = document.getElementById('backToTop');


// ================================================
//  1. MOBILE MENU TOGGLE
//  Clicking the hamburger shows/hides the mobile nav
// ================================================

menuBtn.addEventListener('click', function () {
  // Toggle the "open" class on mobile nav
  mobileNav.classList.toggle('open');

  // Animate the hamburger bars into an X shape
  const bars = menuBtn.querySelectorAll('.menuBar');
  if (mobileNav.classList.contains('open')) {
    bars[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
    bars[1].style.opacity   = '0';
    bars[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
  } else {
    bars[0].style.transform = '';
    bars[1].style.opacity   = '';
    bars[2].style.transform = '';
  }
});

// Close mobile menu when a link is clicked
const mobileNavLinks = document.querySelectorAll('.mobileNavLink');
mobileNavLinks.forEach(function (link) {
  link.addEventListener('click', function () {
    mobileNav.classList.remove('open');
    // Reset hamburger bars
    const bars = menuBtn.querySelectorAll('.menuBar');
    bars[0].style.transform = '';
    bars[1].style.opacity   = '';
    bars[2].style.transform = '';
  });
});


// ================================================
//  2. HEADER SCROLL EFFECT
//  Add a more visible background when user scrolls
// ================================================

window.addEventListener('scroll', function () {
  if (window.scrollY > 60) {
    // Slightly stronger background on scroll
    header.style.background = 'rgba(8, 11, 16, 0.98)';
  } else {
    header.style.background = 'rgba(8, 11, 16, 0.9)';
  }

  // Show/hide the back to top button
  if (window.scrollY > 400) {
    backToTop.classList.add('visible');
  } else {
    backToTop.classList.remove('visible');
  }
});


// ================================================
//  3. BACK TO TOP BUTTON
//  Scrolls smoothly to the very top of the page
// ================================================

backToTop.addEventListener('click', function () {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});


// ================================================
//  4. GAME SEARCH + FILTER
//  Users can search by name AND filter by category
// ================================================

// Keep track of which filter is currently active
let activeFilter = 'all';

// --- Filter buttons (All, Action, RPG, Shooter, Adventure) ---
filterBtns.forEach(function (btn) {
  btn.addEventListener('click', function () {
    // Remove "active" from all buttons, then add it to the clicked one
    filterBtns.forEach(function (b) { b.classList.remove('active'); });
    btn.classList.add('active');

    // Save the chosen filter
    activeFilter = btn.getAttribute('data-filter');

    // Apply both the filter and any current search text
    applyFilterAndSearch();
  });
});

// --- Search input (triggers on every keystroke) ---
searchInput.addEventListener('input', function () {
  applyFilterAndSearch();
});

// --- Main function: shows/hides cards based on filter + search ---
function applyFilterAndSearch() {
  // Get the current search text, lowercase for easy comparison
  const searchText = searchInput.value.toLowerCase().trim();

  let visibleCount = 0; // counts how many cards are showing

  gameCards.forEach(function (card) {
    // Get this card's category and name from its data attributes
    const cardCategory = card.getAttribute('data-category');
    const cardName     = card.getAttribute('data-name').toLowerCase();

    // Check if category matches (or if "all" is selected)
    const categoryMatch = (activeFilter === 'all') || (cardCategory === activeFilter);

    // Check if the search text appears in the card name
    const searchMatch = (searchText === '') || cardName.includes(searchText);

    // Show card only if BOTH conditions are true
    if (categoryMatch && searchMatch) {
      card.style.display = 'block';
      visibleCount++;
    } else {
      card.style.display = 'none';
    }
  });

  // Show the "no results" message if nothing is visible
  if (visibleCount === 0) {
    noResults.style.display = 'block';
  } else {
    noResults.style.display = 'none';
  }
}


// ================================================
//  5. CONTACT FORM VALIDATION
//  Checks all fields before "sending" the message
// ================================================

form1.addEventListener('submit', function (event) {
  // Stop the browser from actually submitting (refreshing the page)
  event.preventDefault();

  // Track if the whole form is valid
  let isValid = true;

  // --- Validate: Name ---
  if (inputName.value.trim() === '') {
    showError('formGroup1', 'nameError');
    isValid = false;
  } else {
    clearError('formGroup1');
  }

  // --- Validate: Email (must look like an email address) ---
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(inputEmail.value.trim())) {
    showError('formGroup2', 'emailError');
    isValid = false;
  } else {
    clearError('formGroup2');
  }

  // --- Validate: Subject ---
  if (inputSubject.value.trim() === '') {
    showError('formGroup3', 'subjectError');
    isValid = false;
  } else {
    clearError('formGroup3');
  }

  // --- Validate: Message (at least 10 characters) ---
  if (inputMessage.value.trim().length < 10) {
    showError('formGroup4', 'messageError');
    isValid = false;
  } else {
    clearError('formGroup4');
  }

  // --- If all valid: hide the form and show success message ---
  if (isValid) {
    form1.style.display = 'none';
    formSuccess.classList.remove('hidden');
  }
});

// Helper: marks a form group as having an error
function showError(groupId, errorId) {
  document.getElementById(groupId).classList.add('hasError');
}

// Helper: removes the error state from a form group
function clearError(groupId) {
  document.getElementById(groupId).classList.remove('hasError');
}

// Live validation: clear errors as user types / fixes them
[inputName, inputEmail, inputSubject, inputMessage].forEach(function (input) {
  input.addEventListener('input', function () {
    // Remove error styling as soon as user starts typing
    const parent = input.closest('.formGroup');
    if (parent) {
      parent.classList.remove('hasError');
    }
  });
});


// ================================================
//  6. CARD ENTRANCE ANIMATIONS
//  Animates game cards and news cards into view
//  using the Intersection Observer API
// ================================================

// Create an observer that watches when elements scroll into view
const observer = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (entry.isIntersecting) {
      // Add a class that triggers the CSS animation
      entry.target.classList.add('animateIn');
      // Stop watching this element once animated
      observer.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.1  // trigger when 10% of the card is visible
});

// Observe all game cards and news cards
document.querySelectorAll('.gameCard, .newsCard, .topItem').forEach(function (el) {
  // Start them invisible and slightly below their final position
  el.style.opacity    = '0';
  el.style.transform  = 'translateY(30px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

  observer.observe(el);
});

// When the observer triggers, animate the element in
document.addEventListener('DOMContentLoaded', function () {
  // We inject a dynamic style for the animateIn class
  const style = document.createElement('style');
  style.textContent = `
    .animateIn {
      opacity: 1 !important;
      transform: translateY(0) !important;
    }
  `;
  document.head.appendChild(style);
});


// ================================================
//  7. ACTIVE NAV LINK HIGHLIGHT
//  Highlights the nav link for whichever section
//  is currently in view as you scroll
// ================================================

const sections  = document.querySelectorAll('section[id]');
const navLinks  = document.querySelectorAll('.navLink');

const sectionObserver = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (entry.isIntersecting) {
      // Remove active from all links
      navLinks.forEach(function (link) { link.style.color = ''; });

      // Highlight the matching link
      const id = entry.target.getAttribute('id');
      const activeLink = document.querySelector('.navLink[href="#' + id + '"]');
      if (activeLink) {
        activeLink.style.color = 'var(--accent)';
      }
    }
  });
}, {
  rootMargin: '-40% 0px -40% 0px'  // trigger near the middle of the screen
});

sections.forEach(function (section) {
  sectionObserver.observe(section);
});


// ================================================
//  DONE! The page is fully interactive.
// ================================================
console.log('🎮 Gaming Hub loaded successfully!');