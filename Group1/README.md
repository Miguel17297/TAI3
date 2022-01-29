# TAI3

Group project for the TAI course inserted into the Masters in Informatics Engineering at Aveiro University



## Getting Started

This requires Python 3.8 or higher.


## Usage
Change to src directory
```bash
cd src
```
### FindMusic

- To execute FindMusic

    ```console
    python3 findmusic.py --s <path_to_sample> -c <compressor_type> --noise_type <type_of_noise> -n <level_of_noise>
    ```

- Usage example:
    ```console
    python3 findmusic.py --s music.wav -c bzip2 --noise_type whitenoise -n 0.2
    ```
- Compressors Available:
    - lzma
    - gzip
    - bzip2
- Type of Noise Available:
    - whitenoise
    - brownnoise

## Authors

 - Pedro Silva (93011)
 - Miguel Almeida (93372)
 - João Soares (93078)
