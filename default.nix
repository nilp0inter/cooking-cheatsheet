{ stdenv, texlive, makeFontsConf, atkinson-hyperlegible }:
stdenv.mkDerivation {
  name = "cheatsheet";
  src = ./.;
  buildInputs = [
    (texlive.combine {
      inherit (texlive) scheme-full collection-latexextra;
    })
  ];
  FONTCONFIG_FILE = makeFontsConf { fontDirectories = [ atkinson-hyperlegible ]; };
  buildPhase = ''
    xelatex cheatsheet.tex
  '';
  installPhase = ''
    cp cheatsheet.pdf $out
  '';
}
