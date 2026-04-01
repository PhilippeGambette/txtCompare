function openDir( form ) { 
	index = form.fieldname.selectedIndex;
	var newIndex = form.fieldname.options[index].value; 
		if ( newIndex == 'false') { 
			alert( "Choisissez un groupe de romans." );
		} else {
			 window.location.assign( newIndex );
		}
	}