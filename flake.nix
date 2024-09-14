{
  description = "This is an environment for my fastapi web app with Python and JavaScript";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python39
            python39Packages.pip
            python39Packages.virtualenv
            python39Packages.fastapi
            python39Packages.uvicorn
            nodejs
            yarn
            nodePackages.npm
          ];

          shellHook = ''
            echo "NutriConnect development environment"
            echo "Run 'cd backend && uvicorn app.main:app --reload' to start the backend"
            echo "Run 'cd frontend && yarn start' to start the frontend"
            echo "Python version: $(python --version)"
            echo "Node.js version: $(node --version)"
            echo "npm version: $(npm --version)"
          '';
        };
      }
    );
}