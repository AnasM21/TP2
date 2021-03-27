const BlogList = ({ blogs, title }) => {
    // 1st way is like this n 2nd one is passing the props into arguments
    // const blogs = props.blogs;
    // const title = props.title;
    return (
        <div className="blog-list">
            <h2>{title}</h2>
             {blogs.map((blog) =>
                <div className="blog-preview" key={blog.id}>
                    <h2>{blog.title}</h2>
                    <p>Written by {blog.author}</p>
                </div>
           )}
        </div>
    );
}
 
export default BlogList;