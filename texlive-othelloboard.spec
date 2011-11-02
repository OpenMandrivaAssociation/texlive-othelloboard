Name:		texlive-othelloboard
Version:	1.2
Release:	1
Summary:	Typeset Othello (Reversi) diagrams of any size, with annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/othelloboard
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/othelloboard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/othelloboard.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package enables the user to generate high-quality Othello
(also known as Reversi) board diagrams of any size. The
diagrams support annotations, including full game transcripts.
Automated board or transcript creation, from plain text formats
standard to WZebra (and other programs) is also supported.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
