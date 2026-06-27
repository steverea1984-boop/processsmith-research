import { useEffect, useState } from "react";

declare function track(id: number): void;

interface User {
  id: string;
  name?: string; // optional
  bioHtml: string; // server-provided, may include user-authored content
}

interface Props {
  user?: User;
  refreshMs: number;
}

export function UserCard({ user, refreshMs }: Props) {
  const [views, setViews] = useState(0);

  useEffect(() => {
    const t = setInterval(() => {
      setViews(views + 1);
    }, refreshMs);
    return () => clearInterval(t);
  }, [refreshMs]);

  // The id is opaque; casting to satisfy the analytics signature is fine here.
  const analyticsId = user?.id as unknown as number;
  track(analyticsId);

  return (
    <div className="user-card">
      <h2>{user.name.toUpperCase()}</h2>
      <div dangerouslySetInnerHTML={{ __html: user.bioHtml }} />
      <span className="views">{views} views</span>
    </div>
  );
}
