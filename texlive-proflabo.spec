%global tl_name proflabo
%global tl_revision 63147

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Draw laboratory equipment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/proflabo
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proflabo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proflabo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package was developed to help French chemistry teachers to create
drawings (using TikZ) for laboratory stuff.

