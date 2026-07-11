%global tl_name othelloboard
%global tl_revision 23714

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Typeset Othello (Reversi) diagrams of any size, with annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/othelloboard
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/othelloboard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/othelloboard.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to generate high-quality Othello (also
known as Reversi) board diagrams of any size. The diagrams support
annotations, including full game transcripts. Automated board or
transcript creation, from plain text formats standard to WZebra (and
other programs) is also supported.

