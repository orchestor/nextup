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
					window.location.href = "/"
				}
			}
		})
	});

	function defaultUserHandle() {
		$('#user-handle-container').removeClass("has-error", "has-success");
		$('.show-wrong').hide();
		$('.show-tick').hide();
		$('.user-handle-error').hide();
	}

	$('#user-handle').focusout(function(){
		var userHandle = $('#user-handle').val();
		if (userHandle === "") {
			defaultUserHandle();
			$('#user-handle-container').addClass("has-error");
			$('.show-wrong').show();
			$('.user-handle-error').text("User handle cannot be blank !");				
		}

		$.ajax({
			type: 'GET',
			url: '/checkUserhandle',
			data: {
				"userHandle": userHandle
			},
			success: function(response) {
				console.log(response)
				if (response["status"] === 1) {
					defaultUserHandle();
					$('#user-handle-container').addClass("has-success");
					$('.show-tick').css('display', 'block');
				} else {
					defaultUserHandle();
					$('#user-handle-container').addClass("has-error");
					$('.show-wrong').css('display', 'block');	
					$('.user-handle-error').show();				
					$('.user-handle-error').text(response["message"]);
				}
			}
		});
	});

	$('#confirm-password').focusout(function(){
		var password = $('#password').val();
		var confirmPassword = $('#confirm-password').val();		
		if (confirmPassword !== password) {
			$('.signup-error').show();
			$('.signup-error').text("Both passwords do not match !");			
		} else {
			$('.signup-error').hide();			
		}
	});

	$('.signup-button').click(function(e){
		e.preventDefault();
		var firstName = $('#first-name').val();
		var userHandle = $('#user-handle').val();
		var age = $('#age').val();
		var email = $('#email').val();
		var gender = $('#gender').val();
		var type = $('#type').val();
		var password = $('#password').val();
		var confirmPassword = $('#confirm-password').val();
		var areaCode = $('#area-code').val();
		var csrftoken = Cookies.get('csrftoken');

		if (confirmPassword !== password) {
			$('.signup-error').show();
			$('.signup-error').text("Both passwords do not match !");			
		}

		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});
		
		$.ajax({
			type: 'POST',
			url: '/signup',
			data: {
				"firstName": firstName,
				"userHandle": userHandle,
				"age": age,
				"email": email,
				"gender": gender,
				"type": type,
				"password": password,
				"areaCode": areaCode
			},
			success: function(response) {
				console.log(response)
				if (response["status"] != 0) {
					$('.signup-error').show();
					$('.signup-error').text(response["message"]);
				} else {
					window.location.href = "/success-signup"
				}
			}
		});
	
	});
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}