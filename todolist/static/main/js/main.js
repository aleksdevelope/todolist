const NOTE = document.getElementsByClassName("note");
const ADD_BUTTON = document.getElementById("add-note");
const SAVE_BUTTON = document.getElementById("save-note");

ADD_BUTTON.onclick = addNote;
NOTE[0].onclick = goNote;
SAVE_BUTTON.onclick = saveNote;

function goNote() {
    window.location.assign('editing_note');
}

function addNote() {
    window.location.assign('editing_note');
}

function saveNote() {
   confirm("Вы уверены что хотите сохранить заметку?");
}