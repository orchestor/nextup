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

	$('.pane1').click(function() {
		if ($('.pause-icon').css("display") === "none") {
			console.log("in play")
			$('.pause-icon').show();
			$('.play-icon').hide();
			var audio = $($(this).find('audio'));
			console.log($(audio[0]))
			audio[0].play();
			$('.container-2').css("background", "url(" + $($(this).find('.song-cover')).html() + ")");
			$('.container-2').css("background-size", "cover");
		} else {
			console.log("in pause")
			$('.pause-icon').hide();
			$('.play-icon').show();
			var audio = $($(this).find('audio'));
			audio[0].pause();			
			$('.container-2').css("background", "#FFEAB3");
			// $('.container-2').css("background-size", "cover");
		}
	});

}