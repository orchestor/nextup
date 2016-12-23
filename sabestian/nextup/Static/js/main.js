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
			'artistName': ($(songAndArtistNames[i]).text()).split("##")[1],
			'numberOfLikes': ($(songAndArtistNames[i]).text()).split("##")[2]
		}
		resultArr.push(temp);
	}
	count = 2
	console.log(resultArr)

	$('.dislike').click(function() {
	    if (count <= resultArr.length) {
			$('.song-name').html(resultArr[resultArr.length - count]['songName']);
			$('.artist-name').html(resultArr[resultArr.length - count]['artistName']);
			$('.like-badge').html(resultArr[resultArr.length - count]['numberOfLikes']);
         } else {
			$('.song-name').html("");
			$('.artist-name').html("");				
			$('.like-badge').html("");
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
			url: '/likeSong',
			data: {
				'songName': $('.song-name').html(),
				'artistName': $('.artist-name').html()
			},
			success: function(response) {
				console.log(response)	
			}
		});
	    if (count <= resultArr.length) {
			$('.song-name').html(resultArr[resultArr.length - count]['songName']);
			$('.artist-name').html(resultArr[resultArr.length - count]['artistName']);
			$('.like-badge').html(resultArr[resultArr.length - count]['numberOfLikes']);
        	console.log(resultArr[resultArr.length - count])
        } else {
			$('.song-name').html("");
			$('.artist-name').html("");				
			$('.like-badge').html("");
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
				$('.like-badge').html(resultArr[resultArr.length - count]['numberOfLikes']);
 	        } else {
				$('.song-name').html("");
				$('.artist-name').html("");				
				$('.like-badge').html("");
	        }
    		var audio = $('audio');
			for(var i = 0; i < audio.length; i++){
				audio[i].pause();
			}
			$('.container-2').css("background", "#FFEAB3");
			$('.pause-icon').hide();
			$('.play-icon').show();

			count += 1;

	    },
		// like callback
	    onLike: function (item) {
		    // set the status text
	        // $('#status').html('Like image ' + (item.index()+1));
	        console.log(count)
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
				url: '/likeSong',
				data: {
					'songName': $('.song-name').html(),
					'artistName': $('.artist-name').html()
				},
				success: function(response) {
					console.log(response)	
				}
			});

    	    if (count <= resultArr.length) {
				$('.song-name').html(resultArr[resultArr.length - count]['songName']);
				$('.artist-name').html(resultArr[resultArr.length - count]['artistName']);
				$('.like-badge').html(resultArr[resultArr.length - count]['numberOfLikes']);
 	        } else {
				$('.song-name').html("");
				$('.artist-name').html("");				
				$('.like-badge').html("");
        	}
			var audio = $('audio');
			for(var i = 0; i < audio.length; i++){
				audio[i].pause();
			}
			$('.container-2').css("background", "#FFEAB3");
			$('.pause-icon').hide();
			$('.play-icon').show();

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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
