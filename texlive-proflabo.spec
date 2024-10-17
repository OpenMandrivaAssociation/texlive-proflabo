Name:		texlive-proflabo
Version:	63147
Release:	2
Summary:	Draw laboratory equipment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/proflabo
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proflabo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proflabo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package was developed to help French chemistry teachers to
create drawings (using TikZ) for laboratory stuff.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/proflabo
%doc %{_texmfdistdir}/doc/latex/proflabo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
