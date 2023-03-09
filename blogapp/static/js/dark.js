 // Function to set the theme
 function setTheme(theme) {
    let navbar = document.querySelector('.navbar');
    let cards = document.querySelectorAll('.card');
  
    if (theme === 'dark') {
      // Set the navbar to dark theme
      navbar.classList.add('black', 'navbar-dark');
      cards.forEach(card => card.classList.add('bg-dark', 'text-white'));
      //set background color
      $("body").css({"background-color": "#1f744e", "color": "white"});
      // Set the cards to dark theme
      
  
      // Store the theme setting in local storage
      localStorage.setItem('theme', 'dark');
    } else {
      // Set the navbar to light theme
      navbar.classList.remove('black', 'navbar-dark');
      cards.forEach(card => card.classList.remove('bg-dark', 'text-white'));
      cards.forEach(card => card.classList.add('text-dark'));

      $("body").css({"background-color": "white", "color": "black"});
      // Set the cards to light theme
     
  
      // Store the theme setting in local storage
      localStorage.setItem('theme', 'light');
    }
  }
  
  // Function to get the saved theme from local storage
  function getSavedTheme() {
    let savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
      setTheme('dark');
    } else {
      setTheme('light');
    }
  }
  var isDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  // Call the getSavedTheme function on page load
  document.addEventListener('DOMContentLoaded', getSavedTheme);
  console.log(isDark);