%define	rname		rdf-redland
Summary:	RDF/Redland module for Ruby
Summary(pl):	Modu� RDF/Redland dla j�zyka Ruby
Name:		ruby-rdf-redland
Version:	0.5.1.3
Release:	1
License:	Ruby
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/1262/%{rname}-%{version}.tgz
# Source0-md5:	fe276ad45b6d58c637c87728806101e6
Source1:	setup.rb
Patch0:		%{name}-tests.patch
URL:		http://librdf.org/docs/ruby.html
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
Requires:	ruby-LOG4R
Requires:	ruby-redland
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDF/Redland module for Ruby.

%description -l pl
Modu� RDF/Redland dla j�zyka Ruby.

%prep
%setup -q -n %{rname}-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}
ruby setup.rb setup

rdoc -o rdoc --inline-source lib
rdoc --ri -o ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%attr(755,root,root) %{ruby_rubylibdir}/rdf/redland*
%{ruby_ridir}/*
