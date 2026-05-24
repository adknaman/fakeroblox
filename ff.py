// Simple click handlers for the UI elements
document.addEventListener('DOMContentLoaded', function() {
    // Log In button
    const loginBtn = document.querySelector('.login-btn');
    loginBtn.addEventListener('click', function() {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        
        if (!username || !password) {
            alert('Please enter username and password');
            return;
        }
        
        loginBtn.textContent = 'Logging in...';
        loginBtn.disabled = true;
        
        // Simulate login process
        setTimeout(() => {
            alert('Login functionality would be implemented here');
            loginBtn.textContent = 'Log In';
            loginBtn.disabled = false;
        }, 1000);
    });
    
    // Forgot Password link
    document.querySelector('.option-link:nth-child(1)').addEventListener('click', function(e) {
        e.preventDefault();
        alert('Forgot password functionality would be implemented here');
    });
    
    // Email One-Time Code link
    document.querySelector('.option-link:nth-child(2)').addEventListener('click', function(e) {
        e.preventDefault();
        alert('One-time code would be sent to email');
    });
    
    // Quick Sign-in
    document.querySelector('.quick-signin').addEventListener('click', function() {
        alert('Quick sign-in would use saved credentials');
    });
    
    // Sign Up link
    document.querySelector('.signup-link').addEventListener('click', function(e) {
        e.preventDefault();
        alert('Redirect to sign up page');
    });
});