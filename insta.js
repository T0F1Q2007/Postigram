const likeIcon = document.querySelector('.like-icon');
likeIcon.addEventListener('click', () => {
  likeIcon.style.color = 'red'; // Change the color to red
  likeIcon.classList.add('liked'); // Add a "liked" class
  likeIcon.removeEventListener('click', handleClick); // Remove the click event listener
});