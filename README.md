# Skimp

> Notmuch email client

[![Build Status](https://travis-ci.org/vhdirk/skimp.svg?branch=master)](https://travis-ci.org/vhdirk/skimp)

An experimental email client based on notmuch, along with other utilities like
afew and offlineimap/isync.

A lot of inspiration comes from [Astroid](https://github.com/astroidmail/astroid) and [alot](https://github.com/pazz/alot).
I like how alot is all command driven. I also like how VSCode/Atom/Textmate work.
So that's probably how I want this thing to work, too.

# Goals
I'm aiming for a nice and full-featured and command-driven UI.

All settings should be stored in easily readable/editable config files, so you
can centralize them in your dotfiles.
While Astroid relies on an external editor for writing emails, I aim for a
default embedded editor. I do like the option of using the editor of your liking, though.

I'd also like for this thing to be modular, so that different UI layers
would be possible. I'd like a ui in GTK, but when I log in remotely, an alot-like
interface would be nice too, I guess.


