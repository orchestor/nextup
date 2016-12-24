document.onready = function() {
	var songAndArtistNames = $('.song-name-artist-name-sub');
	console.log(songAndArtistNames)
	var resultArr = []
	for(var i = 0; i < songAndArtistNames.length; i++) {
		temp = {
			'songName': ($(songAndArtistNames[i]).text()).split("##")[0],
			'artistName': ($(songAndArtistNames[i]).text()).split("##")[1]
		}
		resultArr.push(temp);
	}
	console.log(resultArr)

	var leftBar = false;
	var rightBar = false;

	function increase_width() {
		if (!leftBar && !rightBar) {
			$('.main-part').css("width", "100%");
		} else if(!leftBar && rightBar) {
			$('.main-part').css("width", "66%");			
		} else if (leftBar && !rightBar) {
			$('.main-part').css("width", "80%");
		} else {
			$('.main-part').css("width", "50%");
		}
	}

	$('.genre-icon').click(function() {
		if ($('.sidebar-custom').css("display") === "none") {
			leftBar = true;
			increase_width();
			$('.sidebar-custom').show();
		} else {
			$('.sidebar-custom').hide();
			leftBar = false;
			increase_width();
		}
	});

	$('.heart-like-container').click(function() {
		if ($('.sidebar-custom-right').css("display") === "none") {
			rightBar = true;
			increase_width();
			$('.sidebar-custom-right').show();
		} else {
			$('.sidebar-custom-right').hide();
			rightBar = false;
			increase_width();
		}
	});

	$('.pane1').click(function() {
		if ($('.pause-icon').css("display") === "none") {
			console.log("in play")
			$('.pause-icon').show();
			$('.play-icon').hide();
			var songPath = $($(this).find('.song-file')).html();
			// console.log($(audio[0]))
			// audio[0].play();
			console.log(songPath)
			var audio = $('audio')[0];
			var source = $('source')[0];
			source.src = songPath;
			audio.load();
			audio.play();
			$('.container-2').css("background", "url(" + $($(this).find('.song-cover')).attr("id") + ")");
			$('.container-2').css("background-size", "cover");
		} else {
			console.log("in pause")
			$('.pause-icon').hide();
			$('.play-icon').show();
			var audio = $('audio')[0];
			audio.pause();			
			$('.container-2').css("background", "#FFEAB3");
			// $('.container-2').css("background-size", "cover");
		}
	});

	$('.audio-parent').click(function() {
			$('.pause-icon').hide();
			$('.play-icon').show();
			var songPath = $($(this).find('.song-file-like')).html();
			// console.log($(audio[0]))
			// audio[0].play();
			console.log(songPath)
			var audio = $('audio')[0];
			var source = $('source')[0];
			source.src = songPath;
			audio.load();
			audio.play();
			$('.audio-player-cover').attr("src", $($(this).find('img')).attr("src"));
			$('.container-2').css("background", "#FFEAB3");
	});

	$('.expansion').click(function() {
		window.location.href = "/expansion";
	});
}