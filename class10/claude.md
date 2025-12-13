# Claude Code Project Documentation

## Project Overview

This is a full-stack web application for managing products with a modern glassmorphism UI. The project consists of:
- **Backend**: FastAPI REST API with PostgreSQL database (via Neon)
- **Frontend**: Next.js 16 App Router with React 19, TypeScript, and Tailwind CSS 4

## Technology Stack

### Backend
- **Framework**: FastAPI 0.124.4
- **ORM**: SQLModel 0.0.27 (combines SQLAlchemy + Pydantic)
- **Database**: PostgreSQL (Neon serverless)
- **Python Version**: >=3.14
- **Server**: Uvicorn 0.38.0
- **Dependencies**:
  - `psycopg2` for PostgreSQL connectivity
  - `pydantic` for data validation
  - `python-dotenv` for environment variables
  - `uuid` for unique identifiers

### Frontend
- **Framework**: Next.js 16.0.10 (App Router)
- **React**: 19.2.1
- **TypeScript**: ^5
- **Styling**: Tailwind CSS 4 with @tailwindcss/postcss
- **Fonts**: Geist Sans & Geist Mono (Google Fonts via next/font)
- **Linting**: ESLint 9 with eslint-config-next

## Project Structure

```
class10/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── pyproject.toml          # Python dependencies (uv package manager)
│   ├── uv.lock                 # Lock file for dependencies
│   ├── .python-version         # Python version specification
│   ├── .venv/                  # Virtual environment (ignored in git)
│   └── __pycache__/            # Python cache (ignored in git)
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx            # Home page (Product listing + form)
│   │   ├── layout.tsx          # Root layout with fonts
│   │   └── globals.css         # Global styles + Tailwind imports
│   ├── components/
│   │   ├── GlassForm.tsx       # Client component for adding products
│   │   └── ProductTable.tsx    # Server component for displaying products
│   ├── public/                 # Static assets (SVG icons)
│   ├── package.json            # Node dependencies
│   ├── package-lock.json       # Locked dependency versions
│   ├── tsconfig.json           # TypeScript configuration
│   ├── next.config.ts          # Next.js configuration
│   ├── eslint.config.mjs       # ESLint configuration
│   └── postcss.config.mjs      # PostCSS configuration
│
├── .env                        # Environment variables (DATABASE CREDENTIALS)
├── readme.md                   # Setup instructions
└── data_flow.png               # Architecture diagram
```

## Backend Details

### Database Models

Located in `backend/main.py`:

#### Product Model
```python
class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    in_stock: bool
```

#### Blog Model (Defined but not used in current implementation)
```python
class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
```

### API Endpoints

**Base URL**: `http://localhost:8000`

1. **GET /products**
   - Returns: List of products from in-memory `products_db` array
   - Note: Currently returns hardcoded data, NOT database data

2. **POST /products**
   - Creates new product in PostgreSQL database
   - Body: `{ "name": string, "price": number, "in_stock": boolean }`
   - Auto-generates ID
   - Returns: `{ "message": string, "product": Product }`

3. **DELETE /products/{product_id}**
   - Deletes product from in-memory array (NOT database)
   - Path param: `product_id` (integer)

4. **PUT /products/{product_id}**
   - Updates product in in-memory array (NOT database)
   - Path param: `product_id` (integer)
   - Body: Product object

### CORS Configuration
```python
allow_origins=["*"]           # All origins allowed
allow_credentials=True
allow_methods=["*"]           # All HTTP methods
allow_headers=["*"]           # All headers
```

### Database Configuration

- **Connection String**: Stored in `.env` file as `DATABASE_URL`
- **Provider**: Neon PostgreSQL (serverless)
- **Connection Type**: Pooled connection via pgbouncer
- **Auto-creation**: Tables created on application startup via `create_db_and_tables()`

### Session Management
```python
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
```
Uses dependency injection with FastAPI's `Depends()`.

## Frontend Details

### Components

#### 1. ProductTable (Server Component)
- **Location**: `frontend/components/ProductTable.tsx`
- **Type**: Async Server Component
- **Fetching**: Direct fetch in component (no caching: `cache: "no-store"`)
- **API Call**: `GET http://localhost:8000/products`
- **Rendering**: Server-side table generation

#### 2. GlassForm (Client Component)
- **Location**: `frontend/components/GlassForm.tsx`
- **Type**: Client Component (`"use client"`)
- **State Management**: React useState hooks
- **Features**:
  - Form validation
  - Loading states
  - Error handling
  - Success feedback
  - Auto-refresh after submission using `router.refresh()`
- **API Call**: `POST http://localhost:8000/products`
- **Styling**: Glassmorphism design with backdrop blur

### Routing
- **Architecture**: Next.js App Router
- **Main Route**: `/` (root) → `app/page.tsx`
- **Layout**: Single root layout with Geist fonts

### Styling Approach
- **Framework**: Tailwind CSS 4
- **Import**: Via `@import "tailwindcss"` in `globals.css`
- **Theme**: Inline theme configuration with CSS variables
- **Dark Mode**: Automatic via `prefers-color-scheme`
- **Custom Colors**: Yellow-to-black gradient backgrounds

### TypeScript Configuration
- **Target**: ES2017
- **JSX**: react-jsx
- **Module Resolution**: bundler
- **Path Aliases**: `@/*` maps to root directory
- **Strict Mode**: Enabled

## Environment Variables

### Required Variables (in `.env` at project root)

```env
# Primary database connection (pooled)
DATABASE_URL=postgresql://user:password@host/database?sslmode=require

# Non-pooled connection
DATABASE_URL_UNPOOLED=postgresql://...

# Individual connection parameters
PGHOST=your-host.neon.tech
PGUSER=neondb_owner
PGDATABASE=neondb
PGPASSWORD=your-password

# Vercel/Postgres templates
POSTGRES_URL=postgresql://...
POSTGRES_USER=...
POSTGRES_HOST=...
POSTGRES_PASSWORD=...
POSTGRES_DATABASE=...

# Neon Auth (for Next.js - currently unused)
NEXT_PUBLIC_STACK_PROJECT_ID=****
NEXT_PUBLIC_STACK_PUBLISHABLE_CLIENT_KEY=****
STACK_SECRET_SERVER_KEY=****
```

**IMPORTANT**: The `.env` file contains real credentials and should NEVER be committed to version control.

## Development Setup

### Backend Setup
1. Navigate to `backend/` directory
2. Ensure Python 3.14+ is installed
3. Create virtual environment: `uv venv` or `python -m venv .venv`
4. Activate virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
5. Install dependencies: `uv sync` or `pip install -e .`
6. Ensure `.env` file exists in project root with database credentials
7. Run server: `uvicorn main:app --reload` (from backend directory)
8. API accessible at: `http://localhost:8000`
9. API docs at: `http://localhost:8000/docs` (Swagger UI)

### Frontend Setup
1. Navigate to `frontend/` directory
2. Install dependencies: `npm install`
3. Run dev server: `npm run dev`
4. Application accessible at: `http://localhost:3000`
5. Build for production: `npm run build`
6. Start production server: `npm start`

### Database Setup
1. Create Neon PostgreSQL database via Vercel Storage or neon.tech
2. Copy connection credentials to `.env` file in project root
3. Database tables auto-create on first backend startup
4. View tables and data at: https://neon.com (official dashboard)

## Important Notes & Conventions

### Data Inconsistency Issues

**CRITICAL**: The current implementation has a data inconsistency problem:

1. **GET /products**: Returns hardcoded `products_db` array (in-memory data)
2. **POST /products**: Saves to PostgreSQL database (persistent data)
3. **DELETE/PUT /products**: Modify in-memory array (non-persistent)

**Result**: Frontend displays hardcoded products, not database products. New products saved to DB won't appear in the table.

**Solution Needed**: Update GET endpoint to query database:
```python
@app.get("/products")
def read_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products
```

### Code Quality Issues

1. **Unreachable Code**: Lines 88-90 in `backend/main.py` are unreachable (after return statement)
2. **Missing Import**: `main()` function called in `__main__` block but never defined
3. **Type Safety**: Frontend uses `any` type for products - should define proper TypeScript interface
4. **Error Handling**: Basic error handling in frontend, could be improved

### Security Considerations

1. **CORS**: Currently allows all origins (`*`) - should be restricted in production
2. **Credentials**: `.env` file contains real database credentials
3. **Input Validation**: Limited validation on frontend and backend
4. **SQL Injection**: Protected by SQLModel/SQLAlchemy parameterization

### Naming Conventions

- **Backend**: Snake_case for Python functions/variables
- **Frontend**: camelCase for TypeScript/React
- **Components**: PascalCase for React components
- **Files**: PascalCase for component files, lowercase for config files

### API Contract

**Frontend expects from POST /products response**:
```typescript
{
  message: string;
  product: {
    id: number;
    name: string;
    price: number;
    in_stock: boolean;
  }
}
```

**Frontend expects from GET /products**:
```typescript
Array<{
  id: number;
  name: string;
  description?: string;  // Note: Not in Product model!
  price: number;
  in_stock?: boolean;
}>
```

**Mismatch**: Product model has `in_stock` field, but frontend expects `description` field (not in model).

### Package Managers

- **Backend**: Uses `uv` (modern Python package manager)
- **Frontend**: Uses `npm` (Node package manager)

### Running Both Servers

You need TWO terminal windows:
1. **Terminal 1** (Backend): `cd backend && uvicorn main:app --reload`
2. **Terminal 2** (Frontend): `cd frontend && npm run dev`

## Common Tasks for Claude

### Adding a New Database Model
1. Define SQLModel class in `backend/main.py`
2. Use `SQLModel, table=True` as base classes
3. Add fields with type hints and `Field()` for constraints
4. Tables auto-create on startup

### Adding a New API Endpoint
1. Add function with decorator in `backend/main.py`
2. Use `Depends(get_session)` for database access
3. Update CORS settings if needed for new origins

### Adding a New Page/Route
1. Create new folder in `frontend/app/`
2. Add `page.tsx` for the route content
3. Optionally add `layout.tsx` for route-specific layout

### Adding a New Component
1. Create `.tsx` file in `frontend/components/`
2. Use `"use client"` directive if component needs client-side features
3. Import and use in page components

### Styling Changes
1. Global styles: Edit `frontend/app/globals.css`
2. Component styles: Use Tailwind classes directly in JSX
3. Theme variables: Update CSS variables in `globals.css`

## Testing & Debugging

### Backend Testing
- API documentation: `http://localhost:8000/docs`
- Interactive API testing: Use Swagger UI at `/docs`
- Database inspection: https://neon.com dashboard

### Frontend Testing
- Dev server hot reload: Changes reflect immediately
- React DevTools: Use browser extension
- Network tab: Monitor API calls to backend

## Known Limitations

1. No authentication/authorization
2. No data validation beyond basic type checking
3. No pagination for product lists
4. No search/filter functionality
5. No image upload for products
6. No testing suite (frontend or backend)
7. No CI/CD pipeline
8. No Docker configuration
9. No production deployment configuration
10. Data persistence inconsistency between endpoints (see above)

## Future Improvements to Consider

1. Fix data inconsistency (use database for all CRUD operations)
2. Add proper TypeScript interfaces for Product type
3. Implement proper error handling and logging
4. Add form validation with libraries (Zod, React Hook Form)
5. Add loading skeletons/states
6. Implement optimistic updates
7. Add database migrations (Alembic)
8. Add authentication (Stack Auth variables already in .env)
9. Add API rate limiting
10. Add comprehensive testing
11. Add Docker Compose for local development
12. Add proper environment variable validation
13. Implement proper error pages (404, 500, etc.)
14. Add product image uploads
15. Implement search and filtering
16. Add pagination/infinite scroll

## Quick Reference

### Start Development
```bash
# Terminal 1 - Backend
cd backend
.venv\Scripts\activate  # Windows
uvicorn main:app --reload

# Terminal 2 - Frontend
cd frontend
npm run dev
```

### Access Points
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Database: https://neon.com

### File Locations
- Backend code: `backend/main.py`
- Database config: `.env` (root)
- Frontend pages: `frontend/app/`
- Components: `frontend/components/`
- Styles: `frontend/app/globals.css`
