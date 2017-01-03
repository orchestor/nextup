window.onload = function() {
	$('.follow-unfollow').click(function() {
		console.log($(this).attr("id"))
		if ($(this).attr("id") === "nf") {
			$.ajax({
				url: "/follow",
				type: "GET",
				data: {
					"userHandle": $(".user-handle").text()
				},
				success: function(response) {
					console.log(response)
				}
			});
		} else {
			$.ajax({
				url: "/unfollow",
				type: "GET",
				data: {
					"userHandle": $(".user-handle").text()
				},
				success: function(response) {
					console.log(response)					
				}
			});
		}
	});
}