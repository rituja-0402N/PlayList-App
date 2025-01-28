"use client";

import React, { useEffect, useState } from "react";
import '../../styles/style.css';
import { useParams } from "next/navigation";

type Track = {
    track_id: string,
    title: string;
    artist: string;
    duration: number;
    last_play: string

}
export default function track() {
    const { track_id } = useParams();
    const [track, setTrack] = useState<Track | null>(null);

    useEffect(() => {
        if (track_id) {
            fetch(`http://127.0.0.1:8000/tracks/${track_id}`)
                .then((response) => response.json())
                .then((data) => setTrack(data))
                .catch((error) => console.log(error));
        }
    }, [track_id]);
    return (
        <div>
            <h1>track loading </h1>
            <p><strong>Track ID:</strong> {track_id}</p>
            <p><strong>Track Title:</strong> {track?.title}</p >
            <p><strong>Track Artist: </strong>{track?.artist}</p>
            <p><strong>Track Duration: </strong>{track?.duration}</p>
            <p><strong>Track Last Played: </strong>{track?.last_play}</p>
        </div >
    );
}