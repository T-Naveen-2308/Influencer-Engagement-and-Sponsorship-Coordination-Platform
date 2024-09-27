/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_API_BASE_URL: string;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}

declare global {
    interface User {
        id: string;
        name: string;
        username: string;
        email: string;
        password: string;
        profilePicture: string;
        role: "user" | "librarian";
        requests: Request[];
        feedbacks: Feedback[];
        issuedBooks: IssuedBook[];
        issuedByBooks: IssuedBook[];
    }

    interface Props {}
}

export {};
