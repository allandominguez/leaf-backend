## Initiative Overview
**Initiative Name:** Leaf Mobile App 

**Owner:** Allan Dominguez

**Timeline:** 12-16 weeks (MVP)  

**Status:** [Epic 2: Authentication System](#epic-2-authentication-system) in progress

**Vision Statement:**  
Build a constraint-based, mobile-first note capture app that feels like a physical pocket notebook, demonstrating full-stack product development capabilities from conception to App Store deployment.

**Business Goals:**
1. Ship a production-ready mobile app to Play Store (and optionally App Store)
2. Build portfolio piece demonstrating product-focused engineering
3. Develop job-market-relevant skills (React Native, Django REST APIs, mobile deployment)
4. Validate constraint-based UX hypothesis with real users

**Success Criteria:**
- APK runnable and functional on Android device
- 2+ invite-only beta users providing feedback
- Core user flow (capture → file → expire) fully functional
- Time-to-first-capture < 1 second
- Codebase demonstrates production-ready patterns (testing, CI/CD, error handling)

---

## Epic Breakdown
### Epic 1: Foundation & Environment Setup
**Goal:** Establish development environment and project scaffolding  
**Duration:** 1 week  
**Dependencies:** None

**Stories:**
1. **Local Development Setup**
    - Install Python 3.11+, PostgreSQL, Node.js 18+
    - Set up virtual environment and pip dependencies
    - Configure VS Code / IDE with relevant extensions
    - Acceptance: Can run `python manage.py runserver` successfully
2. **Django Project Initialization**
    - Create Django project with clean structure
    - Set up Django REST Framework
    - Use Django's default SQLite database (migrate to PostgreSQL before deployment)
    - Set up environment variables (python-decouple or django-environ)
    - Acceptance: API returns 200 on `/api/health/` endpoint
3. **React Native Project Setup**
    - Initialize Expo project with TypeScript template
    - Configure folder structure (screens, components, services, types)
    - Set up ESLint and Prettier
    - Acceptance: Can run app on iOS simulator / Android emulator
4. **Version Control & Documentation**
    - Initialize Git repository with .gitignore
    - Create README with setup instructions
    - Set up basic project documentation structure
    - Acceptance: Another developer could clone and run locally

**Epic Acceptance:**
- Backend and frontend run locally without errors
- Basic "Hello World" API call from mobile app to Django works
- Git repository structured and documented

---

### Epic 2: Authentication System
**Goal:** Implement secure user authentication for mobile app  
**Duration:** 1.5 weeks  
**Dependencies:** Epic 1

**Stories:**
1. **Django User Model & Auth Backend**
    - Set up custom User model (or use Django default)
    - Install and configure Django REST Knox
    - Create user registration endpoint
    - Create login endpoint (returns token)
    - Create logout endpoint (invalidates token)
    - Acceptance: Can register, login, logout via API (Postman/curl)
2. **Password Reset Flow (Email-based)**
    - Set up email backend (console for dev, SMTP for prod)
    - Create password reset request endpoint
    - Create password reset confirmation endpoint
    - Acceptance: Can reset password via email link
3. **Mobile Authentication UI**
    - Create welcome/splash screen
    - Create login screen
    - Create registration screen
    - Create forgot password screen
    - Implement form validation
    - Acceptance: UI flows complete, not yet connected to API
4. **Mobile Auth Integration**
    - Set up Axios or Fetch for API calls
    - Implement token storage (SecureStore)
    - Connect login/register forms to Django API
    - Implement auth state management (Context or Zustand)
    - Create authenticated routing (logged in vs logged out screens)
    - Acceptance: Can register, login, and token persists across app restarts
5. **Auth Error Handling**
    - Handle network errors gracefully
    - Display meaningful error messages (invalid credentials, email exists, etc.)
    - Add loading states to forms
    - Acceptance: All error scenarios handled with good UX

**Epic Acceptance:**
- Users can create accounts and log in securely
- Tokens persist across app restarts
- Password reset flow works end-to-end
- Error handling provides clear feedback

---

### Epic 3: Core Note Data Model & API
**Goal:** Build the backend data model and CRUD API for notes  
**Duration:** 2 weeks  
**Dependencies:** Epic 2

**Stories:**
1. **Note Model Design**
    - Create Note model (content, state, created_at, updated_at, user FK)
    - Create Directory model (name, parent FK for nesting, user FK)
    - Define note states (DRAFT, LOOSE, FILED, TRASH)
    - Add photo field (URL/path to external storage)
    - Add metadata fields (is_pinned, is_checklist, page_count)
    - Acceptance: Models created with migrations, admin panel access works
2. **Note CRUD Endpoints**
    - POST /api/notes/ - Create note
    - GET /api/notes/ - List user's notes (with filters)
    - GET /api/notes/{id}/ - Retrieve single note
    - PATCH /api/notes/{id}/ - Update note
    - DELETE /api/notes/{id}/ - Soft delete (move to trash)
    - Acceptance: All endpoints work, return proper data, enforce user ownership
3. **Note State Management Endpoints**
    - POST /api/notes/{id}/file/ - Move to filed (requires directory)
    - POST /api/notes/{id}/pin/ - Toggle pin status
    - POST /api/notes/{id}/restore/ - Restore from trash
    - GET /api/notes/loose/ - Get loose pages only
    - GET /api/notes/filed/ - Get filed notes only
    - GET /api/notes/trash/ - Get trashed notes
    - Acceptance: State transitions work correctly, enforce business rules
4. **Directory CRUD Endpoints**
    - POST /api/directories/ - Create directory
    - GET /api/directories/ - List user's directories (tree structure)
    - PATCH /api/directories/{id}/ - Rename directory
    - DELETE /api/directories/{id}/ - Delete directory (handle filed notes)
    - Validate max 2-level nesting
    - Acceptance: Can create nested directories, enforce depth limit
5. **Business Logic Implementation**
    - Implement notebook size limit (64/96/120/192 pages)
    - Auto-trash oldest loose note when limit exceeded
    - Implement trash expiry (30 days)
    - Implement single-pin rule (unpins previous when pinning new)
    - Acceptance: All constraint rules enforced by backend
6. **API Testing**
    - Write unit tests for models
    - Write API tests for all endpoints
    - Test permission enforcement (users can't access others' notes)
    - Test constraint enforcement
    - Acceptance: >80% test coverage on core endpoints

**Epic Acceptance:**
- All note and directory operations work via API
- Business rules (limits, expiry, single pin) enforced
- Comprehensive test coverage
- API documented (README or Swagger)

---

### Epic 4: Photo Upload & Storage
**Goal:** Enable users to attach one photo per note  
**Duration:** 1 week  
**Dependencies:** Epic 3

**Stories:**
1. **Supabase Storage Setup**
    - Create Supabase project
    - Set up storage bucket for photos
    - Configure bucket policies (authenticated users only)
    - Get API keys and configure in Django settings
    - Acceptance: Can manually upload/download from Supabase dashboard
2. **Django Photo Upload Endpoint**
    - Create POST /api/notes/{id}/upload-photo/ endpoint
    - Accept multipart/form-data
    - Upload to Supabase Storage
    - Return photo URL
    - Update note model with photo URL
    - Implement file size limit (e.g., 5MB)
    - Acceptance: Can upload photo via Postman, URL stored in note
3. **Photo Deletion**
    - Delete photo from Supabase when note deleted
    - Handle photo replacement (delete old, upload new)
    - Acceptance: Photos don't accumulate as orphans
4. **Mobile Photo Capture UI**
    - Add camera permission handling
    - Create photo picker (camera vs gallery)
    - Show photo preview in note editor
    - Implement photo removal
    - Acceptance: Can capture/select photo in app (not yet uploaded)
5. **Mobile Photo Upload Integration**
    - Compress photo before upload (expo-image-manipulator)
    - Upload to Django endpoint
    - Show upload progress
    - Handle upload errors
    - Display uploaded photo in note
    - Acceptance: End-to-end photo flow works

**Epic Acceptance:**
- Users can attach one photo per note
- Photos stored in Supabase
- Photos display in note editor
- Photo size optimized for mobile

---

### Epic 5: Note Editor & Draft Experience
**Goal:** Build the core note-taking interface  
**Duration:** 2 weeks  
**Dependencies:** Epic 3, Epic 4

**Stories:**
1. **Main Editor Screen Layout**
    - Create blank page editor (default screen)
    - Add bottom mode selector (text/checklist/bullet)
    - Hide mode selector when content exists
    - Implement auto-save to draft state
    - Acceptance: Can type and content persists locally
2. **Page Size Constraint UI**
    - Calculate character count
    - Show page fill indicator
    - Block input when page limit reached
    - Show "Continue on new page" prompt
    - Acceptance: Cannot exceed page limit, clear UX feedback
3. **Draft Resume Logic**
    - Detect app switch timing
    - Resume draft if < X minutes
    - Create new page if > X minutes
    - Acceptance: Resume behavior works as spec'd
4. **Checklist Mode**
    - Render checklist items
    - Add new item on Enter
    - Toggle completion on tap/swipe
    - Delete item on swipe
    - Drag to reorder
    - Acceptance: All checklist interactions work
5. **Bullet Mode**
    - Render bullet list items
    - Add new bullet on Enter
    - Handle indentation (optional, may defer)
    - Acceptance: Bullet list creation works
6. **Saving Draft to Backend**
    - Connect editor to API
    - Auto-save draft every 5 seconds (debounced)
    - Save on swipe-down gesture
    - Handle offline (queue saves)
    - Acceptance: Drafts sync to backend
7. **New Page Gesture**
    - Implement swipe-down on filled page
    - Save current page
    - Open new blank page
    - Prevent swipe-down on empty page
    - Acceptance: Gesture creates new note correctly

**Epic Acceptance:**
- Can create text, checklist, and bullet notes
- Page size limits enforced with good UX
- Draft auto-save works reliably
- Resume logic works as expected

---

### Epic 6: Navigation & Panel System
**Goal:** Implement left/right swipe panels for browsing notes  
**Duration:** 1.5 weeks  
**Dependencies:** Epic 5

**Stories:**
1. **Left Panel - Loose Pages Feed**
    - Create swipeable drawer (react-native-gesture-handler)
    - Fetch loose notes from API
    - Display in reverse chronological order
    - Show preview text, timestamp, photo thumbnail
    - Acceptance: Can swipe right to see loose notes
2. **Right Panel - Directory Tree**
    - Create swipeable drawer
    - Fetch directories and filed notes from API
    - Render 2-level tree structure
    - Show only filed notes
    - Acceptance: Can swipe left to see directories and filed notes
3. **Note Actions (Long Press Menu)**
    - Implement long-press gesture on note in panels
    - Show action sheet: Pin / File / Delete
    - File action shows directory picker
    - Acceptance: Can perform actions on notes from panels
4. **Directory Picker Modal**
    - Create directory selection UI
    - Allow creating new directory inline
    - Enforce 2-level max depth
    - Acceptance: Can file notes to directories
5. **Pin Indicator**
    - Show pin icon on pinned note
    - Open pinned note by default (if active)
    - Acceptance: Pinned note clearly indicated and opens on launch
6. **Panel Performance**
    - Implement pagination or lazy loading
    - Add pull-to-refresh
    - Optimize rendering (FlatList virtualization)
    - Acceptance: Smooth scrolling with 100+ notes

**Epic Acceptance:**
- Left/right panels work smoothly
- Can browse, open, and act on notes
- Directory system functional
- Performance acceptable on mid-range devices

---

### Epic 7: Trash & Lifecycle Management
**Goal:** Implement trash, auto-deletion, and note lifecycle  
**Duration:** 1 week  
**Dependencies:** Epic 6

**Stories:**
1. **Trash View**
    - Add trash tab/section
    - Show trashed notes with expiry countdown
    - Implement restore action
    - Implement permanent delete action
    - Acceptance: Can view and manage trashed notes
2. **Auto-Trash Background Job**
    - Set up Django Celery (or Celery Beat)
    - Create task to trash oldest loose note when quota exceeded
    - Create task to permanently delete notes after 30 days
    - Acceptance: Jobs run on schedule, correctly manage note lifecycle
3. **Notebook Size Setting**
    - Add user profile/settings model
    - Create settings screen in mobile app
    - Allow selecting notebook size (64/96/120/192 pages)
    - Sync to backend
    - Acceptance: Changing size affects auto-trash behavior
4. **Quota Indicators**
    - Show "X of Y pages used" in UI
    - Warn when approaching limit
    - Acceptance: User aware of quota status

**Epic Acceptance:**
- Notes automatically expire as designed
- Users can restore or permanently delete
- Notebook size configurable
- Lifecycle state machine works correctly

---

### Epic 8: Search & Filtering
**Goal:** Enable users to find notes quickly  
**Duration:** 1 week  
**Dependencies:** Epic 6

**Stories:**
1. **Backend Search Implementation**
    - Add search parameter to note list endpoints
    - Implement full-text search on content
    - Filter by note type (checklist/text/bullet)
    - Filter by has_photo
    - Acceptance: Search returns relevant results
2. **Mobile Search UI**
    - Add search bar to panels
    - Implement real-time search (debounced)
    - Show search results in panel
    - Add filter chips (checklists, photos)
    - Acceptance: Can search and filter notes
3. **Search Optimization**
    - Add database indexes for search
    - Test search performance with 1000+ notes
    - Acceptance: Search feels instant

**Epic Acceptance:**
- Search works across loose and filed notes
- Filters functional
- Performance acceptable

---

### Epic 9: Polish & Production Readiness
**Goal:** Prepare app for beta release  
**Duration:** 2 weeks  
**Dependencies:** All previous epics

**Stories:**
1. **Error Handling & Offline Support**
    - Implement global error boundary
    - Add retry logic for failed API calls
    - Queue mutations when offline
    - Show offline indicator
    - Acceptance: App doesn't crash, handles offline gracefully
2. **Loading States & Animations**
    - Add skeleton loaders
    - Implement smooth transitions
    - Add haptic feedback (vibrations)
    - Polish swipe gestures
    - Acceptance: App feels responsive and polished
3. **Crash Reporting**
    - Set up Sentry (or similar)
    - Configure source maps
    - Test crash reporting
    - Acceptance: Crashes reported automatically
4. **Analytics Integration**
    - Set up PostHog or Mixpanel
    - Track key events (note_created, note_filed, etc.)
    - Track success metrics (time to first capture)
    - Acceptance: Events flowing to analytics platform
5. **Onboarding Flow**
    - Create welcome slides
    - Add product tour (optional)
    - Set default notebook size
    - Acceptance: New users understand core concepts
6. **Settings & Account Management**
    - Add settings screen
    - Allow changing email, password
    - Add logout functionality
    - Show app version
    - Acceptance: All account management works
7. **App Icon & Splash Screen**
    - Design app icon
    - Create splash screen
    - Configure in Expo
    - Acceptance: Professional branding

**Epic Acceptance:**
- App feels production-ready
- Error handling comprehensive
- Analytics tracking user behavior
- Onboarding explains core concepts

---

### Epic 10: Deployment & Distribution
**Goal:** Ship to Play Store and optionally App Store  
**Duration:** 1-2 weeks  
**Dependencies:** Epic 9

**Stories:**
1. **Migrate SQLite to PostgreSQL**
	- Install psycopg2-binary
	- Update DATABASES setting in settings.py
	- Run migrations on PostgreSQL
	- Export data from SQLite and import to PostgreSQL (if you have real data)
	- Test all functionality still works
	- Acceptance: App runs on PostgreSQL locally before deploying
2. **Backend Deployment**
    - Choose hosting (Railway, Render, Fly.io)
    - Set up production database (managed PostgreSQL)
    - Configure environment variables
    - Set up SSL/HTTPS
    - Configure CORS for mobile app
    - Acceptance: Backend accessible via public URL
3. **Backend Monitoring & Backups**
    - Set up database backups (automated)
    - Configure application monitoring (Sentry, error logs)
    - Set up uptime monitoring (UptimeRobot or similar)
    - Acceptance: Backend monitored and backed up
4. **Mobile App Build Configuration**
    - Configure app.json (version, bundle ID, permissions)
    - Set up EAS Build (Expo Application Services)
    - Create production build
    - Test production build on physical devices
    - Acceptance: Production build works correctly
5. **Play Store Submission**
    - Create Google Play Developer account ($25 one-time)
    - Prepare store listing (description, screenshots, icon)
    - Fill out privacy policy and data safety form
    - Submit for review
    - Acceptance: App published on Play Store
6. **App Store Submission (Optional)**
    - Create Apple Developer account ($99/year)
    - Prepare store listing
    - Submit for review (longer review process)
    - Acceptance: App published on App Store
7. **Beta Testing Program**
    - Set up TestFlight (iOS) or internal testing (Android)
    - Recruit 10+ beta testers
    - Collect feedback
    - Iterate based on feedback
    - Acceptance: Beta feedback incorporated

**Epic Acceptance:**
- Backend deployed and stable
- App available on at least Play Store
- Beta testing complete with feedback
- Monitoring and backups in place

---

### Epic 11: Post-Launch Iteration (Optional)
**Goal:** Improve based on user feedback  
**Duration:** Ongoing  
**Dependencies:** Epic 10

**Stories:**
1. **Analytics Review**
    - Review user behavior data
    - Identify drop-off points
    - Measure success metrics
    - Acceptance: Data-driven insights documented
2. **Feature Improvements**
    - Address top user pain points
    - Optimize slow flows
    - Fix bugs discovered in production
    - Acceptance: User satisfaction improving
3. **Performance Optimization**
    - Profile app performance
    - Optimize bundle size
    - Improve battery usage
    - Acceptance: Performance metrics improved
4. **Additional Features**
    - Export notes to Markdown/Text
    - Widget support
    - Share notes
    - Acceptance: Features shipped based on demand

**Epic Acceptance:**
- App actively maintained
- User feedback loop established
- Continuous improvement

---

## Timeline & Milestones
### Phase 1: Foundation (Weeks 1-3)
- ✅ Epic 1: Setup complete
- ✅ Epic 2: Auth working
- 🎯 **Milestone:** Can create account and log in

### Phase 2: Core Features (Weeks 4-8)
- ✅ Epic 3: Note CRUD complete
- ✅ Epic 4: Photos working
- ✅ Epic 5: Editor functional
- 🎯 **Milestone:** Can capture notes end-to-end

### Phase 3: Navigation & Management (Weeks 9-11)
- ✅ Epic 6: Panels working
- ✅ Epic 7: Lifecycle management
- ✅ Epic 8: Search functional
- 🎯 **Milestone:** Full user experience working

### Phase 4: Launch (Weeks 12-14)
- ✅ Epic 9: Polish complete
- ✅ Epic 10: Deployed to stores
- 🎯 **Milestone:** Public beta live

### Phase 5: Iteration (Week 15+)
- ✅ Epic 11: Ongoing improvements
- 🎯 **Milestone:** Product-market fit achieved

---

## Risk Management
### Technical Risks

|Risk|Impact|Mitigation|
|---|---|---|
|React Native learning curve|Medium|Start with Expo docs, build simple screens first|
|Offline sync complexity|High|Implement simple queue, defer complex conflict resolution|
|Photo storage costs|Low|Use Supabase free tier initially, optimize image sizes|
|Background job setup|Medium|Use simple cron initially, move to Celery later|
|App store rejection|Medium|Follow guidelines carefully, prepare for iteration|

### Product Risks

|Risk|Impact|Mitigation|
|---|---|---|
|Users don't understand constraints|High|Strong onboarding, clear value proposition|
|Note limits feel frustrating|Medium|Make limits configurable, test with users early|
|Too niche / no users|Low|It's a portfolio piece, user count secondary|

### Timeline Risks

|Risk|Impact|Mitigation|
|---|---|---|
|Scope creep|High|Stick to MVP, defer nice-to-haves|
|Underestimating React Native|Medium|Buffer time in schedule|
|Deployment issues|Medium|Deploy early to staging environment|

---

## Resource Requirements
### Development Tools (Free/Low Cost)
- VS Code + extensions
- Expo Go app (free)
- Postman (free tier)
- Git + GitHub (free)

### Third-Party Services
- **Supabase:** Free tier (1GB storage, 500MB database)
- **Sentry:** Free tier (5K errors/month)
- **PostHog:** Free tier (1M events/month)
- **Hosting:** Railway/Render ($5-10/mo)
- **Domain (optional):** $12/year

### App Store Fees
- **Google Play:** $25 one-time
- **Apple App Store:** $99/year (optional)

**Estimated Monthly Cost:** $5-10 (hosting only)  
**Upfront Cost:** $25-124 (store fees)

---

## Success Metrics (Post-Launch)
### Usage Metrics
- Daily Active Users (DAU)
- Weekly Active Users (WAU)
- Notes created per user per week
- % of notes filed vs auto-expired

### Technical Metrics
- Time to first capture < 1 second
- App crash rate < 1%
- API response time p95 < 500ms
- Offline mode success rate > 95%

### Product Metrics
- User retention (Day 1, Day 7, Day 30)
- Feature adoption (checklists, photos, filing)
- NPS or satisfaction score
- App store rating > 4.0

---

## Open Source Considerations
### If Making Open Source
1. **License:** Choose MIT or Apache 2.0 (permissive)
2. **Documentation:** Comprehensive README, architecture docs
3. **Setup:** Docker Compose for easy local dev
4. **Contribution Guide:** CONTRIBUTING.md with guidelines
5. **Code Quality:** Linting, formatting, tests all passing
6. **Security:** No secrets in repo, env variable examples

### Repository Structure

```
pocket-notes/
├── backend/          # Django project
├── mobile/           # React Native app
├── docs/             # Architecture, API docs
├── docker-compose.yml
├── README.md
└── LICENSE
```

### Hosting Options for Open Source
- **Option A:** You host, free for all users (your costs)
- **Option B:** Users self-host (technical barrier)
- **Option C:** Offer free tier + paid tier for hosting
- **Recommended:** Start with A, consider C if popular

---

## Next Steps
### Immediate Actions (Week 1)
1. ✅ Review and approve this initiative plan
2. 🔲 Set up development environment (Epic 1, Story 1)
3. 🔲 Initialize Django project (Epic 1, Story 2)
4. 🔲 Initialize React Native project (Epic 1, Story 3)
5. 🔲 Create GitHub repository (Epic 1, Story 4)

### First Sprint Goal
**Complete Epic 1 and start Epic 2**
- Development environment ready
- "Hello World" API call working
- User registration endpoint functional

### Weekly Cadence (Recommended)
- **Monday:** Review last week, plan this week's stories
- **Daily:** Code, commit progress
- **Friday:** Demo to yourself, document learnings
- **Sunday:** Reflect, adjust plan if needed

---

## Appendix: Learning Resources
### React Native
- [Expo Documentation](https://docs.expo.dev/)
- [React Native Documentation](https://reactnative.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)

### Django REST Framework
- [DRF Documentation](https://www.django-rest-framework.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Classy Django REST Framework](https://www.cdrf.co/)

### Mobile Development
- [React Navigation](https://reactnavigation.org/)
- [Expo Camera](https://docs.expo.dev/versions/latest/sdk/camera/)
- [React Native Gesture Handler](https://docs.swmansion.com/react-native-gesture-handler/)

### Deployment
- [Railway Docs](https://docs.railway.app/)
- [Expo EAS Build](https://docs.expo.dev/build/introduction/)
- [Play Store Publishing](https://developer.android.com/distribute)

---

**Document Version:** 1.0  
**Last Updated:** February 2026  
**Status:** Ready for Development