from moviepy.editor import *
from PIL import Image

def generate_background_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

def add_transition_effect(clips, transition_duration):
    transition_clip = ImageClip(Image.new('RGB', (clips[0].size[0], clips[0].size[1]), color='black')).set_duration(transition_duration)
    transition_clips = [transition_clip]
    for clip in clips[:-1]:
        transition_clips.append(clip)
        transition_clips.append(transition_clip)
    return concatenate_videoclips(transition_clips)

def main():
    # Paramètres
    background_image_path = "background.jpg"
    output_video_path = "output.mp4"
    duration = 10  # Durée totale de la vidéo en secondes
    fps = 30  # Images par seconde
    transition_duration = 0.5  # Durée de la transition en secondes

    # Création de l'image de fond
    background_img = generate_background_image(background_image_path, width=1920, height=1080)

    # Création de la séquence d'images
    clips = []
    for t in range(duration * fps):
        if t % fps == 0:
            black_img = Image.new('RGB', (background_img.width, background_img.height), color='black')
            clips.append(ImageClip(black_img, duration=1/fps))
        else:
            clips.append(ImageClip(background_img, duration=1/fps))

    # Ajout d'effet de transition
    clips_with_transition = add_transition_effect(clips, transition_duration)

    # Création de la vidéo avec la séquence d'images
    final_clip = concatenate_videoclips(clips_with_transition, method="compose")

    # Ajout de la musique de fond
    audio_clip = AudioFileClip("background_music.mp3")
    final_clip = final_clip.set_audio(audio_clip)

    # Écriture de la vidéo résultante
    final_clip.write_videofile(output_video_path, fps=fps)

if __name__ == "__main__":
    main()
from moviepy.editor import *
from PIL import Image

def generate_background_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

def add_transition_effect(clips, transition_duration):
    transition_clip = ImageClip(Image.new('RGB', (clips[0].size[0], clips[0].size[1]), color='black')).set_duration(transition_duration)
    transition_clips = [transition_clip]
    for clip in clips[:-1]:
        transition_clips.append(clip)
        transition_clips.append(transition_clip)
    return concatenate_videoclips(transition_clips)

def main():
    # Paramètres
    background_image_path = "background.jpg"
    output_video_path = "output.mp4"
    duration = 10  # Durée totale de la vidéo en secondes
    fps = 30  # Images par seconde
    transition_duration = 0.5  # Durée de la transition en secondes

    # Création de l'image de fond
    background_img = generate_background_image(background_image_path, width=1920, height=1080)

    # Création de la séquence d'images
    clips = []
    for t in range(duration * fps):
        if t % fps == 0:
            black_img = Image.new('RGB', (background_img.width, background_img.height), color='black')
            clips.append(ImageClip(black_img, duration=1/fps))
        else:
            clips.append(ImageClip(background_img, duration=1/fps))

    # Ajout d'effet de transition
    clips_with_transition = add_transition_effect(clips, transition_duration)

    # Création de la vidéo avec la séquence d'images
    final_clip = concatenate_videoclips(clips_with_transition, method="compose")

    # Ajout de la musique de fond
    audio_clip = AudioFileClip("background_music.mp3")
    final_clip = final_clip.set_audio(audio_clip)

    # Écriture de la vidéo résultante
    final_clip.write_videofile(output_video_path, fps=fps)

if __name__ == "__main__":
    main()
from moviepy.editor import *
from PIL import Image

def generate_background_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

def add_transition_effect(clips, transition_duration):
    transition_clip = ImageClip(Image.new('RGB', (clips[0].size[0], clips[0].size[1]), color='black')).set_duration(transition_duration)
    transition_clips = [transition_clip]
    for clip in clips[:-1]:
        transition_clips.append(clip)
        transition_clips.append(transition_clip)
    return concatenate_videoclips(transition_clips)

def main():
    # Paramètres
    background_image_path = "background.jpg"
    output_video_path = "output.mp4"
    duration = 10  # Durée totale de la vidéo en secondes
    fps = 30  # Images par seconde
    transition_duration = 0.5  # Durée de la transition en secondes

    # Création de l'image de fond
    background_img = generate_background_image(background_image_path, width=1920, height=1080)

    # Création de la séquence d'images
    clips = []
    for t in range(duration * fps):
        if t % fps == 0:
            black_img = Image.new('RGB', (background_img.width, background_img.height), color='black')
            clips.append(ImageClip(black_img, duration=1/fps))
        else:
            clips.append(ImageClip(background_img, duration=1/fps))

    # Ajout d'effet de transition
    clips_with_transition = add_transition_effect(clips, transition_duration)

    # Création de la vidéo avec la séquence d'images
    final_clip = concatenate_videoclips(clips_with_transition, method="compose")

    # Ajout de la musique de fond
    audio_clip = AudioFileClip("background_music.mp3")
    final_clip = final_clip.set_audio(audio_clip)

    # Écriture de la vidéo résultante
    final_clip.write_videofile(output_video_path, fps=fps)

if __name__ == "__main__":
    main()
from moviepy.editor import *
from PIL import Image

def generate_background_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

def add_transition_effect(clips, transition_duration):
    transition_clip = ImageClip(Image.new('RGB', (clips[0].size[0], clips[0].size[1]), color='black')).set_duration(transition_duration)
    transition_clips = [transition_clip]
    for clip in clips[:-1]:
        transition_clips.append(clip)
        transition_clips.append(transition_clip)
    return concatenate_videoclips(transition_clips)

def main():
    # Paramètres
    background_image_path = "background.jpg"
    output_video_path = "output.mp4"
    duration = 10  # Durée totale de la vidéo en secondes
    fps = 30  # Images par seconde
    transition_duration = 0.5  # Durée de la transition en secondes

    # Création de l'image de fond
    background_img = generate_background_image(background_image_path, width=1920, height=1080)

    # Création de la séquence d'images
    clips = []
    for t in range(duration * fps):
        if t % fps == 0:
            black_img = Image.new('RGB', (background_img.width, background_img.height), color='black')
            clips.append(ImageClip(black_img, duration=1/fps))
        else:
            clips.append(ImageClip(background_img, duration=1/fps))

    # Ajout d'effet de transition
    clips_with_transition = add_transition_effect(clips, transition_duration)

    # Création de la vidéo avec la séquence d'images
    final_clip = concatenate_videoclips(clips_with_transition, method="compose")

    # Ajout de la musique de fond
    audio_clip = AudioFileClip("background_music.mp3")
    final_clip = final_clip.set_audio(audio_clip)

    # Écriture de la vidéo résultante
    final_clip.write_videofile(output_video_path, fps=fps)

if __name__ == "__main__":
    main()
from moviepy.editor import *
from PIL import Image

def generate_background_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

def add_transition_effect(clips, transition_duration):
    transition_clip = ImageClip(Image.new('RGB', (clips[0].size[0], clips[0].size[1]), color='black')).set_duration(transition_duration)
    transition_clips = [transition_clip]
    for clip in clips[:-1]:
        transition_clips.append(clip)
        transition_clips.append(transition_clip)
    return concatenate_videoclips(transition_clips)

def main():
    # Paramètres
    background_image_path = "background.jpg"
    output_video_path = "output.mp4"
    duration = 10  # Durée totale de la vidéo en secondes
    fps = 30  # Images par seconde
    transition_duration = 0.5  # Durée de la transition en secondes

    # Création de l'image de fond
    background_img = generate_background_image(background_image_path, width=1920, height=1080)

    # Création de la séquence d'images
    clips = []
    for t in range(duration * fps):
        if t % fps == 0:
            black_img = Image.new('RGB', (background_img.width, background_img.height), color='black')
            clips.append(ImageClip(black_img, duration=1/fps))
        else:
            clips.append(ImageClip(background_img, duration=1/fps))

    # Ajout d'effet de transition
    clips_with_transition = add_transition_effect(clips, transition_duration)

    # Création de la vidéo avec la séquence d'images
    final_clip = concatenate_videoclips(clips_with_transition, method="compose")

    # Ajout de la musique de fond
    audio_clip = AudioFileClip("background_music.mp3")
    final_clip = final_clip.set_audio(audio_clip)

    # Écriture de la vidéo résultante
    final_clip.write_videofile(output_video_path, fps=fps)

if __name__ == "__main__":
    main()
from moviepy.editor import *
from PIL import Image

def generate_background_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

def add_transition_effect(clips, transition_duration):
    transition_clip = ImageClip(Image.new('RGB', (clips[0].size[0], clips[0].size[1]), color='black')).set_duration(transition_duration)
    transition_clips = [transition_clip]
    for clip in clips[:-1]:
        transition_clips.append(clip)
        transition_clips.append(transition_clip)
    return concatenate_videoclips(transition_clips)

def main():
    # Paramètres
    background_image_path = "background.jpg"
    output_video_path = "output.mp4"
    duration = 10  # Durée totale de la vidéo en secondes
    fps = 30  # Images par seconde
    transition_duration = 0.5  # Durée de la transition en secondes

    # Création de l'image de fond
    background_img = generate_background_image(background_image_path, width=1920, height=1080)

    # Création de la séquence d'images
    clips = []
    for t in range(duration * fps):
        if t % fps == 0:
            black_img = Image.new('RGB', (background_img.width, background_img.height), color='black')
            clips.append(ImageClip(black_img, duration=1/fps))
        else:
            clips.append(ImageClip(background_img, duration=1/fps))

    # Ajout d'effet de transition
    clips_with_transition = add_transition_effect(clips, transition_duration)

    # Création de la vidéo avec la séquence d'images
    final_clip = concatenate_videoclips(clips_with_transition, method="compose")

    # Ajout de la musique de fond
    audio_clip = AudioFileClip("background_music.mp3")
    final_clip = final_clip.set_audio(audio_clip)

    # Écriture de la vidéo résultante
    final_clip.write_videofile(output_video_path, fps=fps)

if __name__ == "__main__":
    main()
from moviepy.editor import *
from PIL import Image

def generate_background_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

def add_transition_effect(clips, transition_duration):
    transition_clip = ImageClip(Image.new('RGB', (clips[0].size[0], clips[0].size[1]), color='black')).set_duration(transition_duration)
    transition_clips = [transition_clip]
    for clip in clips[:-1]:
        transition_clips.append(clip)
        transition_clips.append(transition_clip)
    return concatenate_videoclips(transition_clips)

def main():
    # Paramètres
    background_image_path = "background.jpg"
    output_video_path = "output.mp4"
    duration = 10  # Durée totale de la vidéo en secondes
    fps = 30  # Images par seconde
    transition_duration = 0.5  # Durée de la transition en secondes

    # Création de l'image de fond
    background_img = generate_background_image(background_image_path, width=1920, height=1080)

    # Création de la séquence d'images
    clips = []
    for t in range(duration * fps):
        if t % fps == 0:
            black_img = Image.new('RGB', (background_img.width, background_img.height), color='black')
            clips.append(ImageClip(black_img, duration=1/fps))
        else:
            clips.append(ImageClip(background_img, duration=1/fps))

    # Ajout d'effet de transition
    clips_with_transition = add_transition_effect(clips, transition_duration)

    # Création de la vidéo avec la séquence d'images
    final_clip = concatenate_videoclips(clips_with_transition, method="compose")

    # Ajout de la musique de fond
    audio_clip = AudioFileClip("background_music.mp3")
    final_clip = final_clip.set_audio(audio_clip)

    # Écriture de la vidéo résultante
    final_clip.write_videofile(output_video_path, fps=fps)

if __name__ == "__main__":
    main()

