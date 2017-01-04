window.onload = function() {
	$('.follow-unfollow').click(function() {
		console.log($(this).attr("id"))
		var element = $(this)
		if (element.attr("id") === "nf") {
			$.ajax({
				url: "/follow",
				type: "GET",
				data: {
					"userHandle": $(".uh").text()
				},
				success: function(response) {
					console.log($(element.find(".follow-unfollow-image")).attr("src"))
					element.attr("id", "f")
					$(element.find(".follow-unfollow-tag")).text("UnFollow")
					$(element.find(".follow-unfollow-image")).attr("src", "/static/images/closed-chain.png")
				}
			});
		} else {
			$.ajax({
				url: "/unfollow",
				type: "GET",
				data: {
					"userHandle": $(".uh").text()
				},
				success: function(response) {
					console.log(element.find(".follow-unfollow-image"))					
					element.attr("id", "nf")
					$(element.find(".follow-unfollow-tag")).text("Follow")
					$(element.find(".follow-unfollow-image")).attr("src", "/static/images/open-chain.png")
				}
			});
		}
	});

	$('.pause').hide();
	$('.play').click(function() {
		$($(this).parent().find('.pause')).show();
		$($(this).parent().find('.play')).hide();
		var songPath = $($(this).parent().find('.song-file')).html();
		// console.log($(audio[0]))
		// audio[0].play();
		console.log(songPath)
		var audio = $('audio')[0];
		var source = $('source')[0];
		source.src = songPath;
		audio.load();
		audio.play();
		$($(this).parent().parent().find('.song-stopped')).hide();
		$($(this).parent().parent().find('.song-played')).show();
	});

	$('.pause').click(function() {
		$($(this).parent().find('.pause')).hide();
		$($(this).parent().find('.play')).show();
		var audio = $('audio')[0];
		audio.pause();			
		$($(this).parent().parent().find('.song-stopped')).show();
		$($(this).parent().parent().find('.song-played')).hide();
	});

	$('.cart').click(function() {
		songId = $($(this).parent().parent().find(".song-id")).text()
		console.log(songId)
		$.ajax({
			url: "/getPurchaseLinks",
			type: "GET",
			data: {
				"songId": songId
			},
			success: function(response) {
				console.log(response["purchaseLinkArr"].length)
				$('.modal-body').html("")
				html = ""
				for (var i = 0; i < JSON.parse(response["purchaseLinkArr"]).length; i++) {
					purchaseLinkObj = JSON.parse(response["purchaseLinkArr"])[i]
					console.log(i)
					console.log(purchaseLinkObj)
					purchasePortalName = purchaseLinkObj["fields"]["purchasePortalName"]
					purchasePortalLink = purchaseLinkObj["fields"]["purchaseLink"]
					html += "<p>" + purchasePortalName + " - " + purchasePortalLink + "</p>"
				}
				console.log(html)
				$('.modal-body').append(html)
			}
		});
	});
}