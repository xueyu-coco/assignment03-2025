import asyncio
import pyaudio
import numpy as np

# Audio parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Create async queues
input_queue = asyncio.Queue()
output_queue = asyncio.Queue()

# Input callback function
def input_callback(in_data, frame_count, time_info, status):
    input_queue.put_nowait(in_data)
    return (None, pyaudio.paContinue)

# Output callback function  
def output_callback(in_data, frame_count, time_info, status):
    try:
        data = output_queue.get_nowait()
    except asyncio.QueueEmpty:
        # Generate silence
        data = b'\x00' * CHUNK * CHANNELS * 2  # 16-bit = 2 bytes
    return (data, pyaudio.paContinue)

async def audio_processor():
    print("Starting audio loopback processing...")
    print("Please speak into the microphone, you will hear echo from speakers")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            # Get data from input queue
            if not input_queue.empty():
                input_data = await input_queue.get()
                
                # Audio processing code can be added here
                # For example: add echo, change pitch, etc.
                processed_data = input_data
                
                # Put processed data into output queue
                await output_queue.put(processed_data)
            else:
                # If queue is empty, wait briefly
                await asyncio.sleep(0.01)
                
    except KeyboardInterrupt:
        print("Stopping audio processing")

async def main():
    p = pyaudio.PyAudio()
    
    # Open input stream (microphone)
    input_stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        stream_callback=input_callback
    )
    
    # Open output stream (speakers)
    output_stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        frames_per_buffer=CHUNK,
        stream_callback=output_callback
    )
    
    # Start audio streams
    input_stream.start_stream()
    output_stream.start_stream()
    
    # Run audio processor
    await audio_processor()
    
    # Stop and close streams
    input_stream.stop_stream()
    output_stream.stop_stream()
    input_stream.close()
    output_stream.close()
    p.terminate()

if __name__ == "__main__":
    asyncio.run(main())