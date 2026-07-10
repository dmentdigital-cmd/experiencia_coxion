# Design System Strategy: The Culinary Editorial

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Sensory Sommelier."** 

This system transcends the utility of a standard catering platform, positioning itself as a high-end digital editorial. We are moving away from the "grid-and-border" constraints of traditional web design. Instead, the interface should feel like a curated degustation menu: intentional, rhythmic, and deeply tactile. 

By leveraging asymmetric layouts, overlapping high-end photography, and a sophisticated "tonal-layering" approach, we create an experience that feels organic rather than engineered. The design breaks the template look by treating the screen as a physical canvas where elements breathe, stack, and interact with the grace of a fine-dining service.

## 2. Colors: Tonal Depth & The No-Line Rule
The palette is rooted in the earth—forest greens, burnt oranges, and warm neutrals—evoking the raw ingredients and the heat of the kitchen.

*   **Primary (#2b321f) & Secondary (#954905):** Use the deep Forest Green for authority and the Burnt Orange for moments of "flavor" (CTAs, highlights).
*   **The "No-Line" Rule:** Explicitly prohibit the use of 1px solid borders to define sections. Layout boundaries must be established solely through background color shifts. For example, a `surface-container-low` section should sit directly against a `surface` background to define its edge.
*   **Surface Hierarchy & Nesting:** Treat the UI as a series of stacked sheets of fine linen. Use `surface-container-lowest` for the most prominent foreground cards and `surface-dim` for background context. This creates "nested" depth that feels architectural and premium.
*   **The "Glass & Gradient" Rule:** To avoid a flat, "out-of-the-box" appearance, floating navigation elements or modal overlays should use Glassmorphism. Apply a semi-transparent `surface` color with a `backdrop-blur (20px-40px)` to allow the rich food photography underneath to bleed through.
*   **Signature Textures:** For Hero backgrounds and primary action buttons, use a subtle radial gradient transitioning from `primary` (#2b321f) to `primary_container` (#414934). This adds a "visual soul" and a velvet-like finish that flat hex codes cannot replicate.

## 3. Typography: The Editorial Voice
Our typography pairing is a dialogue between heritage and modernity.

*   **Display & Headlines (Newsreader/Abril Fatface):** High-contrast serifs are the "Chef's Signature." They convey elegance and tradition. Use `display-lg` for hero statements with generous letter-spacing to evoke a luxury magazine feel.
*   **Body & Titles (Manrope/Abhaya Libre):** The transition to Manrope for UI elements provides the necessary functional clarity. The "Sophisticated Utility" of Manrope ensures that even at small scales (`body-sm`), the brand feels contemporary.
*   **Hierarchical Intent:** Use extreme scale shifts. A very large `display-md` headline paired with a significantly smaller, wide-tracked `label-md` creates an intentional, curated tension that screams "high-end."

## 4. Elevation & Depth: Tonal Layering
We reject traditional drop shadows in favor of light and material physics.

*   **The Layering Principle:** Depth is achieved by stacking the surface-container tiers. Place a `surface_container_lowest` card on a `surface_container_low` background to create a soft, natural lift without any artificial shadows.
*   **Ambient Shadows:** When a "floating" effect is mandatory (e.g., a primary floating action button), use an extra-diffused shadow: `blur: 32px`, `spread: -4px`, `opacity: 6%`. The shadow color must be a tinted version of `on-surface` (#221a0f), never pure black.
*   **The "Ghost Border" Fallback:** If a divider is required for extreme accessibility, use a "Ghost Border": the `outline-variant` token at 15% opacity. Never use 100% opaque lines.
*   **Glassmorphism:** Use semi-transparent `surface_variant` layers to create a "frosted glass" effect for headers. This softens the interface edges and integrates the UI with the high-resolution culinary imagery.

## 5. Components: Tactile Craft

*   **Buttons:**
    *   **Primary:** A "Velvet" finish using the Forest Green gradient. Roundedness: `md` (0.375rem). No border.
    *   **Secondary:** "Ghost" style. No background, only a `primary` text label with a `surface_tint` hover state.
*   **Cards & Lists:** 
    *   **Strict Rule:** No divider lines. Separate content using vertical white space (32px, 48px, or 64px) or subtle shifts between `surface_container` levels.
    *   **Card Style:** Use `surface_container_low` with a `lg` (0.5rem) corner radius.
*   **Input Fields:**
    *   Minimalist approach. Only a bottom "Ghost Border" (15% opacity) that animates to 100% `secondary` (#954905) on focus. Labels should use `label-md` in a muted `on-surface-variant`.
*   **Culinary Chips:**
    *   For dietary or flavor profiles. Use `surface_container_high` with `full` roundedness. Text should be `label-sm` in all-caps with +0.05em tracking.
*   **Additional Component: The "Signature Reveal":**
    *   An image-reveal component where culinary photos expand or parallax slightly upon scroll, breaking the container bounds to create an organic, unconstrained feel.

## 6. Do's and Don'ts

### Do
*   **DO** use intentional asymmetry. Allow images to bleed off the edge of the screen or overlap between two surface containers.
*   **DO** prioritize negative space. If a layout feels "crowded," double the padding.
*   **DO** use "On-Surface" colors for text to ensure high-contrast readability against the warm neutral backgrounds.

### Don't
*   **DON'T** use 100% black (#000000). Always use the `on_surface` (#221a0f) or `primary` (#2b321f) for dark text to maintain the organic warmth.
*   **DON'T** use standard "Drop Shadows." They feel cheap and "techy." Stick to tonal layering.
*   **DON'T** use vibrant, "neon" colors. Every hue must feel like it could be found in a forest or a spice rack.