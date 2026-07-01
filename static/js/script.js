document.addEventListener('DOMContentLoaded', function() {
    // Initialize Lucide Icons
    lucide.createIcons();

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
