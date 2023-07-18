singing(elon),
playingGuitar(mark),
playingGuiatar(satya),
singing(jeff),

playingGuiatar(elon):-
    happy(elon),

happy(mark):-
    singing(mark),
    playingGuiatar(mark),

happy(satya):-
    singing(satya);
    playingGuiatar(satya),