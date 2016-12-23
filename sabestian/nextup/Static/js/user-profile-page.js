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
	console.log(resultArr)

	count = 2

	$('.dislike').click(function() {
		$('.song-name').html(resultArr[resultArr.length - count]['songName'])
		count += 1;
	});
}