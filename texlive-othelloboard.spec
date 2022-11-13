Name:		texlive-othelloboard
Version:	23714
Release:	1
Summary:	Typeset Othello (Reversi) diagrams of any size, with annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/othelloboard
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/othelloboard.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/othelloboard.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to generate high-quality Othello
(also known as Reversi) board diagrams of any size. The
diagrams support annotations, including full game transcripts.
Automated board or transcript creation, from plain text formats
standard to WZebra (and other programs) is also supported.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/othelloboard/othelloboard.sty
%doc %{_texmfdistdir}/doc/latex/othelloboard/README
%doc %{_texmfdistdir}/doc/latex/othelloboard/example-rose-chps1-2.pdf
%doc %{_texmfdistdir}/doc/latex/othelloboard/example-rose-chps1-2.tex
%doc %{_texmfdistdir}/doc/latex/othelloboard/othelloboard.pdf
%doc %{_texmfdistdir}/doc/latex/othelloboard/othelloboard.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
