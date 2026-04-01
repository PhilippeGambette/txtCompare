function openDir( form ) { 
	index = form.select_text.selectedIndex;
	var newIndex = form.select_text.options[index].value; 
		if ( newIndex != "") { 
			 window.location.assign( newIndex );
		}
	
	}