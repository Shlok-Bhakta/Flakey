{
  description = "Python Textual Application";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      python = pkgs.python3;
      pythonEnv = python.withPackages (ps: with ps; [
        textual
        textual-dev
      ]);
    in
    {
      packages.${system}.default = pkgs.writers.writePython3Bin "textual-app" {
        libraries = [ pythonEnv ];
        flakeIgnore = [ "E501" ];
      } ./main.py;

      devShells.${system}.default = pkgs.mkShell {
        packages = [
          pythonEnv
          pkgs.black
          pkgs.ruff
        ];
      };
    };
}
