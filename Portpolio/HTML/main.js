const typingElement = document.querySelector('.typing');
const words = ['Graphics Design', 'Web Development', 'Django', 'React Developer'];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typingSpeed = 100;

function type() {
    const currentWord = words[wordIndex];
    if (isDeleting) {
        typingElement.textContent = currentWord.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typingElement.textContent = currentWord.substring(0, charIndex + 1);
        charIndex++;
    }

    if (!isDeleting && charIndex === currentWord.length) {
        // Pause at full word
        setTimeout(() => isDeleting = true, 1000);
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
    }

    setTimeout(type, isDeleting ? typingSpeed / 2 : typingSpeed);
}

// Start typing effect on page load
document.addEventListener('DOMContentLoaded', () => {
    type();
});
