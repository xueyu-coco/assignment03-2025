import librosa
import numpy as np
import pygame
import time

class MusicAnalyzer:
    def __init__(self):
        self.beats = []
        self.tempo = 0
        self.energy = 0
        self.mood = "neutral"
        
    def load_audio(self, audio_path):
        """Load audio file and analyze"""
        self.audio_data, self.sr = librosa.load(audio_path)
        print(f"Audio loaded successfully: {len(self.audio_data)} samples, sample rate: {self.sr}Hz")
        
    def extract_features(self):
        """Extract music features with improved accuracy"""
        # Beat and onset analysis
        self.tempo, self.beats = librosa.beat.beat_track(y=self.audio_data, sr=self.sr)
        self.beat_frames = librosa.frames_to_time(self.beats, sr=self.sr)
        self.onset_env = librosa.onset.onset_strength(y=self.audio_data, sr=self.sr)
        self.onset_frames = librosa.onset.onset_detect(onset_envelope=self.onset_env, sr=self.sr)
        self.onset_times = librosa.frames_to_time(self.onset_frames, sr=self.sr)

        # Dynamic energy (frame-wise)
        self.rms = librosa.feature.rms(y=self.audio_data)[0]
        self.energy = np.mean(self.rms)
        self.energy_dynamic = self.rms

        # Spectral features
        self.spectral_centroid = librosa.feature.spectral_centroid(y=self.audio_data, sr=self.sr)[0]
        self.spectral_rolloff = librosa.feature.spectral_rolloff(y=self.audio_data, sr=self.sr)[0]
        self.spectral_contrast = librosa.feature.spectral_contrast(y=self.audio_data, sr=self.sr)

        # MFCCs (Mel-frequency cepstral coefficients)
        self.mfcc = librosa.feature.mfcc(y=self.audio_data, sr=self.sr, n_mfcc=13)

        # Zero-crossing rate
        self.zero_crossings = librosa.feature.zero_crossing_rate(y=self.audio_data)[0]

        # Harmonic features
        self.chroma = librosa.feature.chroma_stft(y=self.audio_data, sr=self.sr)

        # Mood analysis
        self.analyze_mood()

        print(f"Tempo: {self.tempo:.1f} BPM")
        print(f"Energy: {self.energy:.3f}")
        print(f"Mood: {self.mood}")
        print(f"Onsets detected: {len(self.onset_times)}")
        print(f"MFCC shape: {self.mfcc.shape}")
        
    def analyze_mood(self):
        """Simple mood analysis"""
        centroid_mean = np.mean(self.spectral_centroid)
        energy_mean = np.mean(self.rms)
        
        if energy_mean > 0.1 and centroid_mean > 3000:
            self.mood = "energetic"
        elif energy_mean < 0.05 and centroid_mean < 2000:
            self.mood = "calm"
        elif self.tempo > 120:
            self.mood = "happy"
        else:
            self.mood = "neutral"

# Test music analysis
if __name__ == "__main__":
    analyzer = MusicAnalyzer()
    # Can use any MP3 file for testing
    analyzer.load_audio("test_music.mp3")  # Need to prepare test file
    analyzer.extract_features()