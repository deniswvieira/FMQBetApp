/* 
	Created by Denis Vieira
*/
$('document').ready(function(){

	// SUBMIT BTN
	SubmitBtn = $('#id_submit');
	SubmitBtn.removeAttr('type');

	SubmitBtn.click(function(){
		error = 0;
		// USERNAME
		InputUsername = $('#id_username');
		InputUsernameMsg = $('#val_username');
		
		if(InputUsername.val().length > 15 || InputUsername.val() == "") {
			InputUsernameMsg.html("Username cannot have more than 15 characters.");
			error += 1;
		} else {
			InputUsernameMsg.html("");
		}

		// PASSWORD 1
		InputPassword1 = $('#id_password1');
		InputPasswordMsg1 = $('#val_password1');

		if(InputPassword1.val().length < 8) {
			InputPasswordMsg1.html("Password cannot have less that 8 characters.");
			error += 1;
		} else {
			InputPasswordMsg1.html("");
		}


		// PASSWORD 2
		InputPassword2 = $('#id_password2');
		InputPasswordMsg2 = $('#val_password2');
		
		if(InputPassword2.val() != InputPassword1.val()) {
			InputPasswordMsg2.html("Passwords do not match.");
			error += 1;
		} else {
			InputPasswordMsg2.html("");
		}

		if(error <= 0) {
			SubmitBtn.attr('type', 'submit');
			SubmitBtn.click();
		}

	});

});
