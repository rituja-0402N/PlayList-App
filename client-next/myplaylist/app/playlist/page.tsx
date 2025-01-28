"use client";
import { useEffect, useState } from "react";
import '../styles/style.css'
import { useRouter } from "next/navigation";

type Track = {
    id: string;
    title: string;
    artist: string;
    duration: number;
    last_play: string

}

const formatDate = (dateString) => {
    const date = new Date(dateString);
    const options = { year: "numeric", month: "short" }; // Format: "January 2025"
    return date.toLocaleDateString(undefined, options);
};
export default function Playlist() {
    const [data, setData] = useState<Track[]>([]); // State to store fetched data
    const [loading, setLoading] = useState(true);
    const [sortedData, setSortedData] = useState<Track[]>([]); // State to manage sorted data
    const [isSorted, setIsSorted] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const router = useRouter(); // Initialize router
    // Function to fetch data
    useEffect(() => {
        setLoading(true);
        fetch("http://127.0.0.1:8000/tracks")
            .then((response) => response.json())
            .then((data) => { setData(data); setSortedData(data); setError(null) })// Reset error) // Update the state with the fetched data
            .catch((error) =>
                setError(error.message))
            .finally(() => setLoading(false));

    }, []);

    // Conditional rendering based on loading and error states
    if (loading) {
        return <div>Loading...</div>; // Show loading page
    }
    if (error) {
        return <div>Error: {error}</div>; // Show error message
    }
    const handleRowClick = (id: string) => {
        router.push(`/playlist/${id}`); // Navigate to detail page
    };
    const sortTrack = () => {
        const sorted = [...data].sort((a, b) => {
            const dateA = new Date(a.last_play);
            const dateB = new Date(b.last_play);
            return isSorted ? dateA.getTime() - dateB.getTime() : dateB.getTime() - dateA.getTime();
        });
        setSortedData(sorted);
        setIsSorted(!isSorted); // Toggle sorting order
    };
    // Render loading, error, or the fetched data
    return (
        <div>
            <h1>My Playlist</h1>
            <table className="min-w-full border-collapse border border-gray-300">
                <thead>
                    <tr>
                        <th className="border border-gray-300 px-4 py-2">Track ID</th>
                        <th className="border border-gray-300 px-4 py-2">Title</th>
                        <th className="border border-gray-300 px-4 py-2">Artist</th>
                        <th className="border border-gray-300 px-4 py-2">Duration</th>
                        <th
                            className="border border-gray-300 px-4 py-2 cursor-pointer"
                            onClick={sortTrack} // Trigger sorting on click
                        >
                            Last Played {isSorted ? "↑" : "↓"}
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {sortedData.map((track) => (
                        <tr key={track.id}
                            onClick={() => handleRowClick(track.id)} // Navigate to detail page on row click
                            style={{ cursor: "pointer" }}
                        >
                            <td className="border border-gray-300 px-4 py-2">{track.id}</td>
                            <td className="border border-gray-300 px-4 py-2">{track.title}</td>
                            <td className="border border-gray-300 px-4 py-2">{track.artist}</td>
                            <td className="border border-gray-300 px-4 py-2">{track.duration}</td>
                            <td className="border border-gray-300 px-4 py-2">{formatDate(track.last_play)}</td>

                        </tr>
                    ))}
                </tbody>
            </table>
            {/* <ul>
                {data.map((track: any, index: number) => (
                    <li key={index}>
                        <strong>{track.title}</strong> - {track.artist}
                    </li>
                ))}
            </ul> */}


        </div >
    );
}



