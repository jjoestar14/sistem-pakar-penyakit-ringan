document.addEventListener('DOMContentLoaded', function() {
    // Initialize Lucide Icons
    lucide.createIcons();

    // Mobile Hamburger Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            const isOpen = navLinks.classList.toggle('open');
            // Swap icon between menu and X
            const icon = mobileMenuBtn.querySelector('i');
            if (icon) {
                icon.setAttribute('data-lucide', isOpen ? 'x' : 'menu');
                lucide.createIcons();
            }
        });

        // Close menu when a nav link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('open');
                const icon = mobileMenuBtn.querySelector('i');
                if (icon) {
                    icon.setAttribute('data-lucide', 'menu');
                    lucide.createIcons();
                }
            });
        });

        // Close menu when clicking outside the navbar
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.navbar')) {
                navLinks.classList.remove('open');
                const icon = mobileMenuBtn.querySelector('i');
                if (icon) {
                    icon.setAttribute('data-lucide', 'menu');
                    lucide.createIcons();
                }
            }
        });
    }

    // Checkbox and Select logic for Form Diagnosa
    const formDiagnosa = document.getElementById('form-diagnosa');
    
    if (formDiagnosa) {
        const checkboxes = document.querySelectorAll('.gejala-checkbox');
        const btnProses = document.getElementById('btn-proses');
        const loadingOverlay = document.getElementById('loading');

        // Function to check if at least one checkbox is checked
        const updateSubmitButtonState = () => {
            let isChecked = false;
            checkboxes.forEach(cb => {
                if (cb.checked) {
                    isChecked = true;
                }
            });
            btnProses.disabled = !isChecked;
        };

        // Event listener for checkboxes to toggle CF dropdown and update button state
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const cfSelector = this.closest('.gejala-item').querySelector('.cf-selector');
                if (this.checked) {
                    cfSelector.classList.remove('hidden');
                } else {
                    cfSelector.classList.add('hidden');
                }
                updateSubmitButtonState();
            });
        });

        // Form submit animation
        formDiagnosa.addEventListener('submit', function(e) {
            // Check again to prevent empty submission programmatically
            let isChecked = false;
            checkboxes.forEach(cb => {
                if (cb.checked) isChecked = true;
            });
            
            if (!isChecked) {
                e.preventDefault();
                alert("Silakan pilih minimal 1 gejala.");
                return;
            }

            // Show loading overlay
            loadingOverlay.classList.remove('hidden');
        });
    }

    // Flash message auto-hide
    const flashMessages = document.querySelectorAll('.alert');
    if (flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach(msg => {
                msg.style.opacity = '0';
                msg.style.transition = 'opacity 0.5s ease';
                setTimeout(() => {
                    msg.style.display = 'none';
                }, 500);
            });
        }, 5000); // 5 seconds
    }
});
