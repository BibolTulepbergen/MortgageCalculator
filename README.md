# Mortgage Calculator

A Mortgage Calculator application built with Python, Kivy, and KivyMD for Android.

## Features

- Simple and intuitive UI with KivyMD
- Cross-platform support (Android, iOS, Windows, macOS, Linux)
- Built with Python 3.11
- Material Design interface

## Requirements

### Development

- Python 3.11+
- Buildozer
- JDK 17
- Android SDK (API 33)
- Android NDK (r25c)

### Python Dependencies

See `requirements.txt` for Python package dependencies:
- kivy==2.3.0
- kivymd==1.2.0
- pillow
- sdl2_ttf==2.0.15

## Building

### Local Build (Linux/macOS)

```bash
pip install -r requirements.txt
pip install buildozer
buildozer android debug --spec buildozer.spec
```

### 32-bit APK Build

```bash
buildozer android debug --spec buildozer_32.spec
```

### 64-bit APK Build

```bash
buildozer android debug --spec buildozer_64.spec
```

### GitHub Actions Build

The project automatically builds both 32-bit and 64-bit APKs on push to `master` or `main` branch.

APK files are uploaded as artifacts and can be downloaded from the Actions page.

## Project Structure

```
MortgageCalculator/
├── main.py                 # Application entry point
├── buildozer.spec          # Buildozer configuration (32-bit)
├── buildozer_32.spec       # 32-bit specific configuration
├── buildozer_64.spec       # 64-bit specific configuration
├── requirements.txt        # Python dependencies
├── gradle.properties        # Gradle build configuration
├── data/
│   └── logo/
│       ├── logo.png        # Application icon
│       └── tokio.jpg       # Splash screen
└── .github/
    └── workflows/
        └── android.yml     # GitHub Actions workflow
```

## Configuration

### Buildozer Settings

- **Android API**: 33 (Android 13)
- **Minimum API**: 24 (Android 7.0)
- **NDK**: r25c
- **Architectures**: armeabi-v7a (32-bit), arm64-v8a (64-bit)

### Gradle Settings

- JVM Memory: 2048MB (-Xmx2048m)
- Parallel builds enabled
- AndroidX support enabled

## Troubleshooting

### License Acceptance Error

If you see "licenses not accepted" error:
```bash
sdkmanager --licenses
```
Answer "y" to all prompts.

### Out of Memory Error

Increase JVM memory in gradle.properties:
```
org.gradle.jvmargs=-Xmx4096m
```

### Build Cache Issues

Clean the build cache:
```bash
buildozer android clean
rm -rf .buildozer
```

## License

Your License Here

## Support

For issues and questions, please open an issue on GitHub.
