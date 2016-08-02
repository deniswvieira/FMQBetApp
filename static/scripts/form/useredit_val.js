/* 
	Created by Denis Vieira
*/
$('document').ready(function(){

	function isEmptyOrSpaces(str) {
    return str === null || str.match(/^ *$/) !== null;
	}

	loadUsername = $('#id_username').val();
	loadEmail = $('#id_email').val();

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
		InputEmail = $('#id_email');
		InputEmailMsg = $('#val_email');

		if(isEmptyOrSpaces(InputEmail.val())) {
			InputEmailMsg.html("Email cannot be empty.");
			error += 1;
		} else {
			InputEmailMsg.html("");
		}

		if(InputUsername.val() == loadUsername && InputEmail.val() == loadEmail) {
			return
		}

		if(error <= 0) {
			SubmitBtn.attr('type', 'submit');
			SubmitBtn.click();
		}

	});

	$('#copy-link').click(function() {
		text = $('#id_inviteLink').val();
		window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
	});

	$('#ShowInviteLink').click(function() {
		$('#invite_link')[0].style.display = 'block';
		prot = window.location.protocol;
		hostname = window.location.host;
		path = "/accounts/register?inv=";
		invite = $('#id_invite').val();

		link1 = prot.concat(hostname);
		link2 = hostname.concat(path);
		result = link2.concat(invite);

		$('#id_inviteLink').attr('value', result);
	});

});
