jQuery(function($) {
			if (($.browser.msie) || ($.browser.opera))  {
			    	$('#browser-detection-info').modal({onOpen: function (dialog) {
						dialog.overlay.fadeIn('slow', function () {
							dialog.data.hide();
							dialog.container.fadeIn('slow', function () {
								dialog.data.fadeIn('slow');
							});
						});
					}});
			  }
			  $('#information').click(function(e) {
					$("#modal-content").modal({onOpen: function (dialog) {
						dialog.overlay.fadeIn('slow', function () {
							dialog.data.hide();
							dialog.container.fadeIn('slow', function () {
								dialog.data.fadeIn('slow');
							});
						});
					}});
					return false;
				});
			});