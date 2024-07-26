$(document).ready(function() {
    $('#registerForm').on('submit', function(event) {
        event.preventDefault();
        const data = $(this).serialize(); // This includes the CSRF token

        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        // Validate that passwords match
        if (password !== confirmPassword) {
            document.getElementById('passwordError').style.display = 'block';
            return;
        } else {
            document.getElementById('passwordError').style.display = 'none';
            $.ajax({
                url: '',
                method: 'POST',
                data: data,
                success: function(response) {
                        alert('Registration successful!');
                        window.location.href = '/dashboard/';
                    },
                    error: function() {
                        alert('Registration failed. Please try again.');
                }
            });
        }
    });
});
