function createProject(){


	document.getElementById("formcreate").submit();
}
function cancel(){
	displaything = document.getElementById("cancelpopup").style.display;
	if(displaything =="none"){
		document.getElementById("cancelpopup").style.display = "";

	}
	else{
		document.getElementById("cancelpopup").style.display = "none";

	}

}
function yescancel(){
	window.location.assign("/")
}