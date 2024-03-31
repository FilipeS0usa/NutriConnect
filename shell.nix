{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
  buildInputs = [
    python311Packages.django
  ];

  # In case you need to run a command after virtual shell initiates
  #shellHook = ''
  # Something
  #'';

}
