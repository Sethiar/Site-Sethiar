document.addEventListener('DOMContentLoaded', () => {
    const logoElement = document.getElementById('logo');
    const sprites = logoElement.querySelectorAll('.sprite');
    let currentSprite = 0;

    const spriteDurations = [4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500]; // Durée de chaque sprite

    // Initialisation : masquer tous les sprites sauf le premier
    sprites.forEach((sprite, index) => {
        sprite.style.visibility = index === 0 ? 'visible' : 'hidden';
        sprite.style.animation = 'none'; // Stoppe toute animation en cours
    });

    // Fonction pour démarrer l'animation d'un sprite
    function startAnimation(spriteIndex) {
        const sprite = sprites[spriteIndex];
        sprite.style.visibility = 'visible'; // Affiche le sprite
        sprite.style.animation = `animateLogo${spriteIndex + 1} ${spriteDurations[spriteIndex] / 1000}s steps(20, end) forwards`; // Lancer l'animation
    }

    // Fonction pour arrêter l'animation d'un sprite
    function stopAnimation(spriteIndex) {
        const sprite = sprites[spriteIndex];
        sprite.style.animation = 'none'; // Stoppe l'animation immédiatement
        sprite.style.visibility = 'hidden'; // Cache le sprite
    }

    // Fonction pour gérer la rotation des sprites
    function changeLogo() {
        // Arrête le sprite actuel
        stopAnimation(currentSprite);

        // Passer au sprite suivant
        currentSprite = (currentSprite + 1) % sprites.length;

        // Démarre le sprite suivant
        startAnimation(currentSprite);

        // Planifie le changement au sprite suivant après sa durée
        setTimeout(changeLogo, spriteDurations[currentSprite]);
    }

    // Initialisation : démarrer le premier sprite
    startAnimation(currentSprite);

    // Planifier le premier changement
    setTimeout(changeLogo, spriteDurations[currentSprite]);
});