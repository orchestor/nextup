window.onload = function() {
	swipeStart = false;
	swipeEnd = false;
	$('.cover3').click(function() {
		console.log("up")
		swipeStart = true;
		swipeEnd = true;
	});

	$('.cover3').mousedown(function() {
		console.log("down")
		swipeEnd = true;
		swipeStart = true;
	});

	$(document).mousemove(function(event) {
		if (swipeStart && swipeEnd) {
			console.log(event.pageY)
			if (event.pageY < 400) {
				$('.cover3').css('visibility', 'hidden');
			}
		}
	});
}