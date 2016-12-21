window.onload = function() {
	$('.login-button').click(function(e){
		e.preventDefault();
		var email = $('#login-email').val()
		var password = $('#login-password').val()
		var csrftoken = Cookies.get('csrftoken');
		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
		
		$.ajax({
			type: 'POST',
			url: '/login',
			data: {
				"email": email,
				"password": password
			},
			success: function(response) {
				console.log(response)
				if (response['status'] === 0) {
					$('.login-alert').css('display', 'block');
					$('.login-alert').text(response["message"])
				} else {
					
				}
			}
		})
	});
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}