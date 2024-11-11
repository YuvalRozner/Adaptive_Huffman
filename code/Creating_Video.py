import moviepy.editor as mp
import os
from tqdm import tqdm

def create_video(image_folder, output_video, fps=1, image_duration=0.5, batch_size=50):
    # List all the images in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    # Sort the images by filename (to maintain sequence)
    images.sort()
    
    # Create batches of image clips
    batches = [images[i:i + batch_size] for i in range(0, len(images), batch_size)]
    
    batch_videos = []
    for i, batch in enumerate(tqdm(batches, desc="Processing batches")):
        image_clips = [mp.ImageClip(os.path.join(image_folder, img)).set_duration(image_duration) for img in batch]
        batch_video = mp.concatenate_videoclips(image_clips, method="compose")
        batch_output = f'batch_{i}.mp4'
        batch_video.write_videofile(batch_output, fps=fps)
        batch_videos.append(batch_output)
    
    # Concatenate all batch videos
    final_clips = [mp.VideoFileClip(batch) for batch in batch_videos]
    final_video = mp.concatenate_videoclips(final_clips, method="compose")
    final_video.write_videofile(output_video, fps=fps)
    
    # Clean up temporary batch files
    for batch in batch_videos:
        os.remove(batch)

speed = 2
create_video('C:/Users/gr062/OneDrive/שולחן העבודה/huffman/images', f'output_video_fps{speed}.mp4', fps=speed, image_duration=0.5, batch_size=50)
