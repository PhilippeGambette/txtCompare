$(document).ready(function(){

	$(".popup_1 a").hover(function() {
	$(this).next("em").stop(true, true).animate({opacity: "show", top: "-60"}, "slow");
	}, function() {
	$(this).next("em").animate({opacity: "hide", top: "-70"}, "fast");
	});
	
	$(".popup_2 a").hover(function() {
	$(this).next("em").stop(true, true).animate({opacity: "show", top: "-60"}, "slow");
	}, function() {
	$(this).next("em").animate({opacity: "hide", top: "-70"}, "fast");
	});

});