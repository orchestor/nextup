/**
 * jTinder initialization
 */
window.onload = function() {
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
	count = 2
	console.log(resultArr)

	$('.dislike').click(function() {
	    if (count <= resultArr.length) {
			$('.song-name').html(resultArr[resultArr.length - count]['songName']);
			$('.artist-name').html(resultArr[resultArr.length - count]['artistName']);
        } else {
			$('.song-name').html("");
			$('.artist-name').html("");				
        }
        console.log(count)
		// count += 1;
		var audio = $('audio');
		for(var i = 0; i < audio.length; i++){
			audio[i].pause();
		}
		$('.container-2').css("background", "#FFEAB3");
		$('.pause-icon').hide();
		$('.play-icon').show();
	});

	$('.like').click(function() {
	    if (count <= resultArr.length) {
			$('.song-name').html(resultArr[resultArr.length - count]['songName']);
			$('.artist-name').html(resultArr[resultArr.length - count]['artistName']);
        } else {
			$('.song-name').html("");
			$('.artist-name').html("");				
        }
        console.log(count)
		// count += 1;
		var audio = $('audio');
		for(var i = 0; i < audio.length; i++){
			audio[i].pause();
		}
		$('.container-2').css("background", "#FFEAB3");
		$('.pause-icon').hide();
		$('.play-icon').show();
	});

	$("#tinderslide").jTinder({
		// dislike callback
	    onDislike: function (item) {
		    // set the status text
		    console.log("aaab")
	        // $('#status').html("anaaaaaanaaannnnnnnnanaaaaaa");
	        console.log(count)
	        if (count <= resultArr.length) {
				$('.song-name').html(resultArr[resultArr.length - count]['songName']);
				$('.artist-name').html(resultArr[resultArr.length - count]['artistName']);
	        } else {
				$('.song-name').html("");
				$('.artist-name').html("");				
	        }
    		var audio = $('audio');
			for(var i = 0; i < audio.length; i++){
				audio[i].pause();
			}
			$('.container-2').css("background", "#FFEAB3");

			count += 1;

	    },
		// like callback
	    onLike: function (item) {
		    // set the status text
	        // $('#status').html('Like image ' + (item.index()+1));
	        console.log(count)
    	    if (count <= resultArr.length) {
				$('.song-name').html(resultArr[resultArr.length - count]['songName']);
				$('.artist-name').html(resultArr[resultArr.length - count]['artistName']);
	        } else {
				$('.song-name').html("");
				$('.artist-name').html("");				
	        }
			var audio = $('audio');
			for(var i = 0; i < audio.length; i++){
				audio[i].pause();
			}
			$('.container-2').css("background", "#FFEAB3");

			count += 1;
	    },
		animationRevertSpeed: 200,
		animationSpeed: 400,
		threshold: 1,
		likeSelector: '.like',
		dislikeSelector: '.dislike'
	});

	/**
	 * Set button action to trigger jTinder like & dislike.
	 */
	$('.actions .like, .actions .dislike').click(function(e){
		e.preventDefault();
		$("#tinderslide").jTinder($(this).attr('class'));
	});
}

